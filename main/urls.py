from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.home, name="home"),
    path('details/<int:id>/', views.detail, name="detail"),
    path('addbusiness/', views.add_business, name="add_business"),
    path('editbusiness/<int:id>/', views.edit_business, name="edit_business"),
    path('deletebusiness/<int:id>/', views.delete_business, name="delete_business"),
    path('addreview/<int:id>/', views.add_review, name="add_review"),
    path('editreview/<int:business_id>/<int:review_id>/', views.edit_review, name="edit_review"),
    path('deletereview/<int:business_id><int:review_id>/', views.delete_review, name="delete_review")


]