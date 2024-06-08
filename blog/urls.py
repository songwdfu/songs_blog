# blog/urls.py
# for mapping request to views for app
from . import views
from django.urls import path

urlpatterns = [
      path('', views.PostList.as_view(), name='home'),
      path('create_post', views.create_post, name='create_post'),
      path('<slug:slug>', views.PostDetail.as_view(), name='post_detail')
]