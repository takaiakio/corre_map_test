from django.urls import path
from . import views

urlpatterns = [
    path('', views.correlation_view, name='correlation_view'),
]
