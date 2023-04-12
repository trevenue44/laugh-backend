from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .serializers import RegisterSerializer


class RegisterView(GenericAPIView):
    # setting the serializer class as the register serializer
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        print(request.data)
        if serializer.is_valid():
            # serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response()
