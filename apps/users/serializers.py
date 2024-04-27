from rest_framework import serializers

from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ('id', 'username', 'first_name', 
                  'last_name', 'email', 'date_joined')
        
class UserRegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=255, write_only=True)
    class Meta:
        model = User 
        fields = ('id', 'username', 'first_name', 
                  'last_name', 'age', 'email', 'phone_number', 'password', 'confirm_password')
        
    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({'password':'Пароли отличаются'})
        if '+996' not in attrs['phone_number']:
            raise serializers.ValidationError({'phone_number':'Введённый номер не соответсвует стандартам КР (+996)'})
        return attrs 
    
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            age=validated_data['age'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user