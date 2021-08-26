from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from profiles_app import serializers
from profiles_app import models
from profiles_app import permissions



class HelloAPIView(APIView):
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """ Returns a list of APIView """
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete, etc)',
            'Is Similar to a traditional django view', 
            'Gives you the most control over your application logic.',
            'Is mapped manually to URLs',
        ]

        return Response({"message":"Hello","an_apiview":an_apiview})


    def post(self,request):
        """ create a Hello message with name """
        serializer = self.serializer_class(data=request.POST)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({
                'message': message,
            })
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

    def put(self,request,pk=None):
        """ Handle Updating an object """
        return Response({"method":"PUT"})

    def patch(self,request,pk=None):
        """ Handle partially updating an object """
        return Response({"method":"PATCH"})

    def delete(self,request,pk=None):
        """ Delete an object """
        return Response({"method":"DELETE"})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self,request):
        """Return a hello message"""
        a_viewset = [
            "Uses Actions (list, Create, Retrieve, Update, Delete)",
            "Automatically map to URL through Router", 
            "Provide more functionality with less code",
        ]

        return Response({"message":"Hello", "a_viewset":a_viewset})

    def create(self, request):
        """ Create a new hello message """
        serializer = self. serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({"message": message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST,
            )

    def retrieve(self, request, pk=None):
        """ Handle getting an object with an ID""" 
        return Response({"http_method":"GET"})

    def update(self, request, pk=None):
        """ Handle Updating an object"""
        return Response({"http_method":"PUT"})

    def partial_update(self, request, pk=None):
        """ Updating data Partially """
        return Response({"http_method":"PATCH"})

    def destroy(self, request, pk=None):
        """Deleting an object with an ID"""
        return Response({"http_method":"DELETE"})


class UserProfileViewSet(viewsets.ModelViewSet):
    """ Handle Creating and Updating Profiles """
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("name","email",)