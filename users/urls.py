from django.urls import path
from .views import UserView


urlpatterns = [
    path('userapi/', UserView.as_view()),
]