from django.urls import path, include
from rest_framework.routers import SimpleRouter

from receipt_generator_api.views.auth.register_view import AuthenticationViewset
from receipt_generator_api.views.auth.login_view import LoginViewset


router = SimpleRouter()

router.register("auth", AuthenticationViewset, basename="register")
router.register("auth", LoginViewset, basename="login")

urlpatterns = [
    path('',include(router.urls))
]

