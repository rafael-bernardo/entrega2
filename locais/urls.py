from django.urls import path
from . import views

app_name = 'locais'

urlpatterns = [
    path('', views.LocaisList.as_view(), name='lista_locais'),
    path('<int:pk>/', views.LocaisDetail.as_view(), name='detail_locais'),
    path('create/', views.LocaisCreate.as_view(), name='create_locais'),
    path('<int:pk>/update/', views.LocaisUpdate.as_view(), name='update_locais'),
    path('<int:pk>/delete/', views.LocaisDelete.as_view(), name='delete_locais'),
    path('<int:pk>/comment_create/', views.comment_create, name='comment_create'),
    path('categories/<int:category_id>/', views.category_detail, name='category_detail'),
    path('categories/', views.category_list, name='category_list'),
]