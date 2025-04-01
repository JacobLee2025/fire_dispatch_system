from django.urls import path
from .views import dispatch_form_view

urlpatterns = [
    path('', dispatch_form_view, name='dispatch_form'),
]
