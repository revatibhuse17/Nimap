from django.urls import path
from . import views

urlpatterns = [
    path('user_projects/', views.user_projects),
    path('client_list/', views.client_list),
    path('edit_client/<int:client_id>/', views.edit_client),
    path('delete_client/<int:client_id>/', views.delete_client),  
    path('register_client/', views.register_client),
    path('delete_client/<int:client_id>/', views.delete_client),
]

