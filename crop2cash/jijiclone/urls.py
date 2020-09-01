from django.urls import path, include, re_path
from rest_framework import routers
from rest_framework.authtoken import views as auth_views
from . import views

app_name = "jijiclone"


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('signup', views.SignUpView.as_view(), name='signup'),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('items/<int:pk>', views.ItemView.as_view(), name='items-update'),
    path('items', views.ItemView.as_view(), name='items'),
    re_path(r'item-detail', views.ItemDetailView.as_view(), name='item-detail'),
    # url(r'api-token-auth', auth_views.obtain_auth_token, name='api-token-auth')
]