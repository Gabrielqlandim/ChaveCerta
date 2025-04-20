from djoser.views import UserViewSet
from .serializers import CustomUserCreateSerializer, CustomUserSerializer
from .models import CustomUser
from .permissions import IsSelfOrReadOnly

class CustomUserViewSet(UserViewSet):
    queryset = CustomUser.objects.all()
    permission_classes = [IsSelfOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'create':
            return CustomUserCreateSerializer  # Usa CustomUserCreateSerializer ao criar usuário
        return CustomUserSerializer  # Usa CustomUserSerializer no restante
