from django.urls import path
from .views import index, add_user,UserListCreateView, UserDetailsView

urlpatterns = [
    path('', index, name='index'),
    path('add_user/', add_user, name='add_user'),
    path('api/users/', UserListCreateView.as_view(), name='user-list-create'),
    path('api/users/<int:pk>/', UserDetailsView.as_view(), name='user-details'),
]
