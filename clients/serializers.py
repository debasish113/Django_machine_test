from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Client, Project

class UserSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class ProjectSerializer(serializers.ModelSerializer):
    users = UserSimpleSerializer(many=True, read_only=True)
    users_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=User.objects.all(), write_only=True, source='users'
    )

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'users', 'users_ids', 'created_at', 'created_by']
        read_only_fields = ['id', 'created_at', 'created_by']

class ClientListSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()
    class Meta:
        model = Client
        fields = ['id', 'client_name', 'created_at', 'created_by']

class ClientDetailSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()
    projects = ProjectSerializer(many=True, read_only=True)
    class Meta:
        model = Client
        fields = ['id', 'client_name', 'projects', 'created_at', 'updated_at', 'created_by']
