from django.urls import path
from .views import signin

urlpatterns = [
    path('signin/', signin, name='signin'),  # Add a URL to signin page
]
