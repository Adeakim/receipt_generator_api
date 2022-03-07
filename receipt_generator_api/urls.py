from django.urls import path, include
from rest_framework.routers import DefaultRouter

from receipt_generator_api.views.auth.register_view import AuthenticationViewset


router = DefaultRouter()

router.register("register", AuthenticationViewset, basename="register")

urlpatterns = [
    path('',include(router.urls))
]

