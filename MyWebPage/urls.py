from django.urls import path
from . import views

app_name = 'mywebpage'

urlpatterns = [
    path('', views.home, name='home'),
    # Add other paths here
]
