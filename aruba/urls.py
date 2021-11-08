from django.urls import path

from aruba.forms import RegistrationForm

from . import views

urlpatterns = [
    path('', views.index, name='all-switches'),
    path('<slug:switches_slug>/success', views.confirm_registration, name='confirm-registration'),
    path('<slug:switches_slug>', views.switches_details, name='switches-detail'),
]