
from django.urls import path, include
from .views import (home, 
                    plan, 
                    join, 
                    checkout, 
                    settings, 
                    SignUp)


urlpatterns = [
    path('', home, name='home'),
    path('plans/<int:pk>', plan, name='plan'),
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/signup', SignUp.as_view(), name='signup'),
    path('join', join, name='join'),
    path('checkout', checkout, name="chsckout"),
    path('auth/settings', settings, name='settings')
]
