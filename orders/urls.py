from django.urls import path
from .views import OrderView, PrInOrderView


urlpatterns = [
    path('orderapi/', OrderView.as_view()),
    path('prinorder/api/', PrInOrderView.as_view()),
]