from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('post_detail/<int:id>/', views.post_detail, name='post_detail'),
    path('category_detail/<int:id>/', views.category_detail, name='category_detail'),
    path('login/', views.login, name='login'),
    path('user_like_post/', views.user_like_post, name='user_like_post'),
]