from django.db import models
import uuid

# Create your models here.
class Tax_Admin(models.Model):
	public_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
	name = models.CharField(max_length = 50)
	email = models.EmailField(max_length = 50, unique = True)
	phone = models.IntegerField(unique = True)
	pan_number = models.CharField(max_length = 10, unique = True)
	password = models.CharField(max_length = 100)

	def __str__(self):
		return self.name

class Tax_Accountant(models.Model):
	public_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
	name = models.CharField(max_length = 50)
	email = models.EmailField(max_length = 50, unique = True)
	phone = models.IntegerField(unique = True)
	pan_number = models.CharField(max_length = 10, unique = True)
	password = models.CharField(max_length = 100)

	def __str__(self):
		return self.name

class Tax_Payer(models.Model):
	public_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
	name = models.CharField(max_length = 50)
	gst_number = models.CharField(max_length = 15, unique = True)
	pan_number = models.CharField(max_length = 10, unique = True)
	email = models.EmailField(max_length = 50, unique = True)
	phone = models.IntegerField(unique = True)
	password = models.CharField(max_length = 100)

	def __str__(self):
		return self.name

class Tax(models.Model):
	payer = models.ForeignKey(Tax_Payer, on_delete = models.CASCADE)
	sgst = models.CharField(max_length = 10, null = True)
	cgst = models.CharField(max_length = 10, null = True)
	ugst = models.CharField(max_length = 10, null = True)
	arrears = models.CharField(max_length = 10, null = True)
	fines = models.CharField(max_length = 10, null = True)
	income = models.CharField(max_length = 10)
	texable_amount = models.CharField(max_length = 10)

	def __str__(self):
		return self.texable_amount