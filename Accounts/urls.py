from django.urls import path
from . import views


urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.log_in,name='login'),
    path('logout/',views.log_out,name='logout'),
    path('update_password/',views.update_password,name='update_password'),
    path('profile/',views.edit_profile,name='profile'),
    
]
