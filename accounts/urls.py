#accounts/urls.py - Added by Adam S.
from django.urls import path
from .views import SignUpView

urlpatterns = [
    path("signup/",SignUpView.as_view(), name="signup"),
]