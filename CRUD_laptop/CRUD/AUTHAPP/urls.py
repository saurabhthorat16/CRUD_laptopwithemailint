from django.urls import path
from . import views

urlpatterns = [
    path('reg/', views.registerView, name='register_url'),
    path('log/', views.loginView, name='login_url'),
    path('logout/', views.logoutView, name='logout_url'),
    path("verify/", views.twostepView, name='verify')
]