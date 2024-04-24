from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from apps.base.models import Todo
from apps.base.serializers import TodoSerializer

# Create your views here.
class TodoAPI(ListCreateAPIView, DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoRetrive(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated, )