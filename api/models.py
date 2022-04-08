from django.db import models

# Create your models here.
class Tax_Admin(models.Model):
	name = models.CharField(max_length = 50)
	email = models.EmailField(max_length = 50, unique = True)
	phone = models.IntegerField(unique = True)
	pan_number = models.CharField(max_length = 10, primary_key = True)
	password = models.CharField(max_length = 100)

	def __str__(self):
		return self.name

class Tax_Accountant(models.Model):
	name = models.CharField(max_length = 50)
	email = models.EmailField(max_length = 50, unique = True)
	phone = models.IntegerField(unique = True)
	pan_number = models.CharField(max_length = 10, primary_key = True)
	password = models.CharField(max_length = 100)

	def __str__(self):
		return self.name

class Tax_Payer(models.Model):
	name = models.CharField(max_length = 50)
	gst_number = models.CharField(max_length = 15)
	pan_number = models.CharField(max_length = 10, primary_key = True)
	email = models.EmailField(max_length = 50)
	phone = models.IntegerField(unique = True)
	password = models.CharField(max_length = 100)

	def __str__(self):
		return self.name

class Tax(models.Model):
	payer = models.ForeignKey(Tax_Payer, on_delete = models.CASCADE)
	sgst = models.CharField(max_length = 10)
	cgst = models.CharField(max_length = 10)
	ugst = models.CharField(max_length = 10, null = True)
	arrears = models.CharField(max_length = 10, null = True)
	fines = models.CharField(max_length = 10, null = True)
	income = models.CharField(max_length = 10)
	texable_amount = models.CharField(max_length = 10)

	def __str__(self):
		return self.texable_amount