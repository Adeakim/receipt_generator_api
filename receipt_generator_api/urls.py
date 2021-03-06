from django.urls import path, include
from rest_framework.routers import SimpleRouter

from receipt_generator_api.views.auth.register_view import AuthenticationViewset,UserViewset
from receipt_generator_api.views.auth.login_view import LoginView
from receipt_generator_api.views.generate_receipt_view import GenerateReceiptViewset


router = SimpleRouter()

router.register("auth", AuthenticationViewset, basename="register")
router.register("users", UserViewset, basename="users")
# router.register("auth", LoginView, basename="login")
router.register("generate-receipt", GenerateReceiptViewset, basename="generate-receipt")

urlpatterns = [
    path('',include(router.urls)),
    path("auth/login", LoginView.as_view(), name="login")
]

