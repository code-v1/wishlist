from django.urls import path
from .import views 


urlpatterns = [
    # path('', views.home, name='home'),
    path('add/', views.ItemCreate.as_view(), name='item_create'),
    path('', views.ItemList.as_view(), name='item_list' ),
    path('delete_confirm', views.ItemDelete.as_view(), name='item_delete'),
]