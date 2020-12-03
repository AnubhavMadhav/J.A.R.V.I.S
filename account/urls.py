from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('contact', views.contact, name='contact'),
    path('signup', views.handleSignup, name='signup'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('login', views.handleLogin, name='login'),
    path('logout', views.handleLogout, name='logout'),
    path('mail', views.sendmail, name='mail'),
    path('jarvis', views.jarvis, name='jarvis'),
    path('trial', views.trial, name='trial'),
    path('whatsapp', views.sendWhatsApp, name='whatsapp'),
]