from django.urls import path, include
from myapp.views import *

urlpatterns = [
    path('', admin_login, name='admin_login'),
    path('accounts/login/', admin_login, name='admin_login'),
    path('logout/', logout_user, name='logout_user'),
    path('home/', admin_home, name='admin_home'),
     path('college/',clg, name='admin_home1'),
    path('eee/', eee, name='admin_home1'),
     path('ece/', ece, name='admin_home1'),
    path('cse/', cse, name='admin_home1'),
    path('device-control/', device_control, name='device_control'),
    path('get-stat/', get_stat, name='get_stat'),
    path('send-stat/', send_stat, name='send_stat'),
]
