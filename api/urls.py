from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()

# admin Api
router.register('register/admin', views.RegisterAdminAPI, basename = 'RegisterAdminAPI')
router.register('login/admin', views.LoginAdminAPI, basename = 'LoginAdminAPI')
router.register('accountant', views.AccountantAPI, basename = 'AccountantAPI')

# accountant api
router.register('register/accountant', views.RegisterAccountantAPI, basename = 'RegisterAccountantAPI')
router.register('login/accountant', views.LoginAccountantAPI, basename = 'LoginAccountantAPI')

# payer api
router.register('register/payer', views.RegisterPayerAPI, basename = 'RegisterPayerAPI')
router.register('login/payer', views.LoginPayerAPI, basename = 'LoginPayerAPI')


# admin and accountant api
router.register('payer', views.PayerAPI, basename = 'PayerAPI')


router.register('tax', views.TaxAPI, basename='TaxAPI')


# Admin, Accountant and Payer API's
#router.register('profile', views.ProfileAPI, basename = 'ProfileAPI')

urlpatterns = [
    path('', include(router.urls))
]