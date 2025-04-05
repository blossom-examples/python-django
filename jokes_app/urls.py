from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('jokes/', views.joke_list, name='joke_list'),
    path('jokes/<int:pk>/', views.joke_detail, name='joke_detail'),
    path('jokes/new/', views.joke_create, name='joke_create'),
    path('jokes/<int:pk>/edit/', views.joke_update, name='joke_update'),
    path('jokes/<int:pk>/delete/', views.joke_delete, name='joke_delete'),
    path('random/', views.random_joke, name='random_joke'),
]