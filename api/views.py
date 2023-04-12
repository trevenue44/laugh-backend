from rest_framework import status
from rest_framework import views
from rest_framework.response import Response


class HomeView(views.APIView):
    def get(self, request):
        return Response({"message": "Welcome to LAUGH🤣"}, status=status.HTTP_200_OK)
