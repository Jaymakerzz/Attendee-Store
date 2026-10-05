from djoser.serializers import UserCreateSerializer as BasecreateSerializer

class UserCreateSerializer(BasecreateSerializer):
    class Meta(BasecreateSerializer.Meta):
        fields = ['id', 'username', 'first_name', 'last_name', 'password']