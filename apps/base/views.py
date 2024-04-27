from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from apps.base.models import Todo
from apps.base.serializers import TodoSerializer, ToDoCreateSerializer
from apps.base.permissions import ToDoPermission

# Create your views here.
class TodoAPI(ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
    def get_serializer_class(self):
        if self.request.method == "POST":
            return ToDoCreateSerializer
        return TodoSerializer

class TodoRetrive(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated, )

    def get_permissions(self):
        if self.request.method in ('DELETE', 'PUT', 'PATCH'):
            return (ToDoPermission(), )
        return (AllowAny(), )