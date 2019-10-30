from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('product/', views.products_list),
    path('product/<int:id>/', views.products_show),
    path('product/create/', views.product_create),
    path('product/<int:id>/card/', views.save_card),
    path('product/cart/', views.cart),
    path('product/finalizar/', views.final)
 

]