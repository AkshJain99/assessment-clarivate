from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.models import Users 
from accounts.serializers import UsersSerializer  

class UserListView(APIView):
    def get(self, request):
        users = Users.objects.all()
        serializer = UsersSerializer(users, many=True)
        return Response(serializer.data)
