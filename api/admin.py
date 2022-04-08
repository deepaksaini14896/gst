from django.contrib import admin
from api.models import Tax_Admin, Tax_Accountant, Tax_Payer, Tax

# Register your models here.
admin.site.register(Tax_Admin)
admin.site.register(Tax_Accountant)
admin.site.register(Tax_Payer)
admin.site.register(Tax)