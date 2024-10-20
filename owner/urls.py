from django.urls import path
from . import views
urlpatterns = [
    path('owner_home/', views.owner_home, name='owner_home'),
    path('add_category/', views.add_category, name='add_category'),
    path('add_blog/', views.add_blog, name='add_blog'),
]