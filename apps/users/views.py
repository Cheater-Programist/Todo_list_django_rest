from rest_framework.generics import ListCreateAPIView

from apps.users.models import User
from apps.users.serializers import UserSerializer, UserRegisterSerializer

# Create your views here.
class UserAPI(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        print(self.request.method == "POST")
        if self.request.method == "POST":
            return UserRegisterSerializer
        return UserSerializer