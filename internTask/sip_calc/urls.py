from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sip_calculate', views.sip_calculate, name='sip_calculate'),
    path('num_until_depleted/', views.num_until_depleted, name='num_until_depleted'),
    path('total_withdrawn/', views.total_withdrawn, name='total_withdrawn'),
    path('transactions/', views.transactions, name='transactions'),
]