from django.shortcuts import render
from  rest_framework import mixins
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.generics import GenericAPIView
from .serializers import TodoSerializer, TodoCreateSerializer
from .models import  Todo
from django.http import JsonResponse


class TodoView(generics.ListAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all().order_by('-id')

def give_data_of_this_id(request, pk):
    todos = Todo.objects.get(id=pk)
    print(todos)
    serializer = TodoSerializer(todos)
    return JsonResponse(serializer.data)



class create_todo(GenericAPIView, mixins.CreateModelMixin ):
    serializer_class = TodoCreateSerializer
    def post(self, request, *args, **kwargs):
        print(request.POST.get('data'))
        return self.create(request, *args, **kwargs)