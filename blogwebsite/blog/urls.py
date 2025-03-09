from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('blogs/', views.blogs, name='blogs'),
    path('createblog/', views.createblog, name='create-blog'),
    path('singleblog/<int:pk>', views.singleblog, name='single-blog'),
    path('delete/<int:pk>', views.deleteblog, name='delete-blog'),
    path('edit/<int:pk>', views.editblog, name='edit-blog'),
]