from  django.urls import path
from .views import ProductView


urlpatterns = [
    path('productapi/', ProductView.as_view()),
]