from django.urls import path, include

from petstagram.photos import views

urlpatterns = [
    path('add/', views.add_photo, name='add_photo'),
    path('<int:pk>/', views.photo_details, name='photo_detail'),
    path('<int:pk>/edit/', views.photo_edit, name='photo_edit'),
]