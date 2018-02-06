from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.insert, name='create'),
    path('retrieve/', views.find, name='retrieve'),
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
]
