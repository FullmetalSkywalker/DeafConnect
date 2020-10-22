from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.home, name="home"),
    path('details/<int:id>/', views.detail, name="detail"),
    path('addbusiness/', views.add_business, name="add_business"),
    path('editbusiness/<int:id>/', views.edit_business, name="edit_business"),
    path('deletebusiness/<int:id>/', views.delete_business, name="delete_business"),
]
