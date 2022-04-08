from rest_framework.serializers import ModelSerializer
from .models import Tax_Admin, Tax_Accountant, Tax_Payer, Tax

class Tax_AdminSerializer(ModelSerializer):
	class Meta:
		model = Tax_Admin
		fields = '__all__'

class Tax_AccountantSerializer(ModelSerializer):
	class Meta:
		model = Tax_Accountant
		fields = '__all__'

class Tax_PayerSerializer(ModelSerializer):
	class Meta:
		model = Tax_Payer
		fields = '__all__'

class Tax_Serializer(ModelSerializer):
	class Meta:
		model = Tax
		fields = '__all__'
