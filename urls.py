from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    path('base/',views.base, name='base'),
    path('welcm/',views.welcm, name='welcm'),
    path('signup/',views.signup, name='signup'),
    path('dash/',views.dash, name='dash')
]