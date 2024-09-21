from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('countries/', views.country_list, name='country_list'),
    path('states/', views.state_list, name='state_list'),
    path('cities/', views.city_list, name='city_list'),
    path('userprofiles/', views.userprofile_list, name='userprofile_list'),
    path('sportcategories/', views.sportcategory_list, name='sportcategory_list'),
    path('equipments/', views.equipment_list, name='equipment_list'),
    path('productcarts/', views.productcart_list, name='productcart_list'),
    path('orders/', views.order_list, name='order_list'),
    path('payments/', views.payment_list, name='payment_list'),
    path('feedbacks/', views.feedback_list, name='feedback_list'),
    path('contacts/', views.contactus_list, name='contactus_list'),

]
