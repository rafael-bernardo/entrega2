from django.urls import path
from . import views

app_name = 'locais'

urlpatterns = [
    path('', views.lista_locais, name='lista_locais'),
    path('<int:pk>/', views.detail_locais, name='detail_locais'),
    path('create/', views.create_locais, name='create_locais'),
    path('update/<int:pk>/', views.update_locais, name='update_locais'),
    path('delete/<int:pk>/', views.delete_locais, name='delete_locais'),
]