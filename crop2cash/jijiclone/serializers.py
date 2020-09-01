from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import CustomUser, Item, Buyer

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        password = validated_data.get('password')
        validated_data.pop('password')
        # validated_data.pop('is_active')
        return CustomUser.objects.create(
            is_active=True,
            password=make_password(password),
            **validated_data
        )


    class Meta:
        model = CustomUser
        fields = (
            'id','email','first_name','last_name','is_active',
            'state_of_residence','password','username'
        )
        extra_kwargs = {
            'password': {'write_only': True},
            'username': {'write_only': True},
            'is_active': {'write_only': True}
        }

class ItemSerializer(serializers.ModelSerializer):
    def update(self, instance, validated_data):
        instance.sold_status = validated_data['sold_status']
        instance.save()
        return instance

    class Meta:
        model = Item
        exclude = ('buyers',)
        extra_kwargs = {
            'user': {'write_only': True},
        }

class BuyerSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        email = validated_data.get('email')
        validated_data.pop('email')
        buyer, _ = Buyer.objects.get_or_create(
            email=email, defaults={**validated_data}
        )
        return buyer

    class Meta:
        model = Buyer
        fields = '__all__'
        extra_kwargs = {
            'email': {'validators': []},
        }        

class ItemDetailSerializer(ItemSerializer):
    buyers = BuyerSerializer(many=True, read_only=True)

    class Meta:
        model = Item
        fields = '__all__'
        extra_kwargs = {
            'user': {'write_only': True},
        }

class ItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        exclude = ('buyers','sold_status','mark_delete','user')
        extra_kwargs = {
            'name': {'read_only': True},
            'price': {'read_only': True},
            'description': {'read_only': True},
            'image': {'read_only': True},
        }
