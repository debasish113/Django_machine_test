from rest_framework import viewsets, generics, permissions, status
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from django.contrib.auth.models import User
from .models import Client, Project
from .serializers import ClientListSerializer, ClientDetailSerializer, ProjectSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientListSerializer

    def get_serializer_class(self):
        if self.action in ['retrieve']:
            return ClientDetailSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ClientProjectCreateAPIView(generics.CreateAPIView):
    serializer_class = ProjectSerializer

    def perform_create(self, serializer):
        client = get_object_or_404(Client, pk=self.kwargs['client_id'])
        serializer.save(client=client, created_by=self.request.user)

class ProjectsAssignedToUserListAPIView(generics.ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return self.request.user.projects.all()
