from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response



class HelloAPIView(APIView):

    def get(self, request, format=None):
        """ Returns a list of APIView """
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete, etc)',
            'Is Similar to a traditional django view', 
            'Gives you the most control over your application logic.',
            'Is mapped manually to URLs',
        ]

        return Response({"message":"Hello","an_apiview":an_apiview})