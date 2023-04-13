from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from django.contrib.auth import authenticate

from . import serializers


class RegisterView(GenericAPIView):
    # setting the serializer class as the register serializer
    serializer_class = serializers.RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        # if the serializer is not valid, return the errors.
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(GenericAPIView):
    serializer_class = serializers.LoginSerializer

    def post(self, request):
        # getting credentials from the request data
        username = request.data["username"]
        password = request.data["password"]
        # authenticating the laugher based on provided credentials
        laugher = authenticate(username=username, password=password)
        # if user is authenticated...
        if laugher:
            data = self.serializer_class(laugher).data
            return Response(data=data, status=status.HTTP_200_OK)
        else:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
