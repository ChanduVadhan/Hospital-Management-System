from django.urls import path

from authen import views


urlpatterns=[
    path('',views.login_,name='login_'),
    path('register/',views.register,name='register'),
    path('logout_',views.logout_,name='logout_'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('change_password/', views.changepassword, name='change_password'),
    path('profile/',views.profile,name='profile'),
  
]