from django.urls import path
from . import views

urlpatterns = [
    path('lp/', views.laptopFormView, name='laptopform_url'),
    path('sl/', views.showlaptopView, name='showlaptop_url'),
    path('up/<int:id>/', views.updateLaptopView, name='updatelaptop_url'),
    path('dl/<int:id>/', views.deleteLaptopView, name='deletelaptop_url')

]
