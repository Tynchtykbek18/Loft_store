from rest_framework.permissions import IsAdminUser
from rest_framework import generics
from users.models import CustomUser
from users.serializers import UserSerializer


# Create your views here.
class UserView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser, )