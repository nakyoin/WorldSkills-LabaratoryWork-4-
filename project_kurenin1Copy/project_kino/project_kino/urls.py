from django.contrib import admin
from films import views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('add/', views.add),
    path('edit/', views.edit),
    path('delete/', views.delete),
]
