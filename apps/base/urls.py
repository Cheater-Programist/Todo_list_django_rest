from django.urls import path 

from apps.base.views import TodoAPI, TodoRetrive

urlpatterns = [
    path('', TodoAPI.as_view(), name="api_todo"),
    path('<int:pk>/', TodoRetrive.as_view(), name="api_todo_detail")
]