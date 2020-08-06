from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

from rest_framework.decorators  import api_view
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import UserSerializer, UserSerializerWithToken

@api_view(['GET'])
def current_user(request):
    print(request.user)
    serilaizer = UserSerializer(request.user)
    return Response(serilaizer.data, )

class UserList(APIView):
    permission_classes = (permissions.AllowAny,)    
    def post(self, request):
        print(request.data)
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
