from django.contrib.auth import get_user_model
from rest_framework import status, permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    lookup_field = 'id'
    serializer_class = UserSerializer
    queryset = User.objects.all()

    @action(detail=False, methods=["GET"])
    def me(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @action(detail=False, methods=["GET"])
    def logout(self, request):
        request.user.auth_token.delete()
        return Response({'status': True, 'message': 'Se ha cerrado sesion.'}, status=status.HTTP_200_OK)
