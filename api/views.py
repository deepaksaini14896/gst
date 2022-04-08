from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .models import Tax_Admin, Tax_Accountant, Tax_Payer, Tax
from .serializers import Tax_AdminSerializer, Tax_AccountantSerializer, Tax_PayerSerializer, Tax_Serializer
from utils import create_password, check_password, create_token
from django.db.models import Q
import jwt

# Create your views here.
class RegisterAdminAPI(ViewSet):
	def create(self,request):
		#Take password for hashing
		password = request.data['password']
		request.data['password'] = create_password(password)
		serializers = Tax_AdminSerializer(data = request.data)

		if serializers.is_valid():
			serializers.save()
			return Response( { "Message" : "Admin Added" } )

		return Response(serializers.errors)

class RegisterAccountantAPI(ViewSet):
	def create(self,request):
		#Take password for hashing
		password = request.data['password']
		request.data['password'] = create_password(password)
		serializers = Tax_AccountantSerializer(data=request.data)

		if serializers.is_valid():
			serializers.save()
			return Response( { "Message" : "Accountant Added" } )

		return Response(serializers.errors)

class RegisterPayerAPI(ViewSet):
	def create(self,request):
		#Take password for hashing
		password = request.data['password']
		request.data['password'] = create_password(password)
		serializers = Tax_PayerSerializer(data=request.data)

		if serializers.is_valid():
			serializers.save()
			return Response({"Message":"Payer Added"})

		return Response(serializers.errors)

class AccountantAPI(ViewSet):
	def list(self,request):
		act = Tax_Accountant.objects.all()
		serializers = Tax_AccountantSerializer(act, many = True)
		return Response(serializers.data)

	def retrieve(self,request,pk):
		act = Tax_Accountant.objects.get(pan_number = pk)
		serializers = Tax_AccountantSerializer(act)
		
		if serializers.is_valid():
			return Response(serializers.data)
		
		return Response({"Message": "not found"})

	def update(self, request, pk):
		act = Tax_Accountant.objects.all()
		serializers = Tax_AccountantSerializer(act, data = request.data)

		if serializers.is_valid():
			return Response(serializers.data)
		
		return Response( { "Message" : "Accountant Profile Updated" } )

	def partial_update(self, request, pk):
		act = Tax_Accountant.objects.all()
		serializers = Tax_AccountantSerializer(act, data = request.data, partial = True)

		if serializers.is_valid():
			return Response(serializers.data)

		return Response( { "Message" : "Accountant Profile Updated" } )


class PayerAPI(ViewSet):
	def list(self,request):
		pyr = Tax_Payer.objects.all()
		serializers = Tax_PayerSerializer(pyr, many=True)
		return Response(serializers.data)

class TaxAPI(ViewSet):
	def create(self,request):
		serializers = Tax_Serializer(data=request.data)

		if serializers.is_valid():
			serializers.save()
			return Response({"Message":"Tax Due Create"})

		return Response(serializers.errors)

	def list(self,request):
		tx = Tax.objects.all()
		serializers = Tax_Serializer(tx, many=True)
		return Response(serializers.data)

class LoginAdminAPI(ViewSet):
	def create(self, request):
		try:
			adm = Tax_Admin.objects.get( Q(email = request.data['email_or_phone'] ) | Q(phone = request.data['email_or_phone'] ))
		except DoesNotExist:
			return Response( { "Message" : "User not found" } )

		if check_password(request.data['password'], adm.password):
			token = create_token(adm.pan_number)
			return Response( { "Token" : token } )

		return Response( { "Message" : "Password doesn't match" } )

class LoginAccountantAPI(ViewSet):
	def create(self, request):
		try:
			act = Tax_Accountant.objects.get( Q(email = request.data['email_or_phone'] ) | Q(phone = request.data['email_or_phone'] ))
		except DoesNotExist:
			return Response( { "Message" : "User not found" } )

		if check_password(request.data['password'], act.password):
			token = create_token(act.pan_number)
			return Response( { "Token" : token } )

		return Response( { "Message" : "Password doesn't match" } )

class LoginPayerAPI(ViewSet):
	def create(self, request):
		try:
			pyr = Tax_Payer.objects.get( Q(email = request.data['email_or_phone'] ) | Q(phone = request.data['email_or_phone'] ))
		except DoesNotExist:
			return Response( { "Message" : "User not found" } )

		if check_password(request.data['password'], pyr.password):
			token = create_token(pyr.pan_number)
			return Response( { "Token" : token } )

		return Response( { "Message" : "Password doesn't match" } )