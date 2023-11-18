from rest_framework import viewsets, status
from rest_framework.response import Response

from users.serializers import UserSerializer
from users.models import User


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data

        telegram_id = data.get('telegram_id')
        if not telegram_id:
            return Response({"telegram_id": "Это поле обязательное"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
