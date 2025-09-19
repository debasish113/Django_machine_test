from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, ClientProjectCreateAPIView, ProjectsAssignedToUserListAPIView

router = DefaultRouter()
router.register(r'clients', ClientViewSet, basename='client')

urlpatterns = [
    path('', include(router.urls)),
    path('clients/<int:client_id>/projects/', ClientProjectCreateAPIView.as_view(), name='client-project-create'),
    path('projects/', ProjectsAssignedToUserListAPIView.as_view(), name='user-projects'),
]
