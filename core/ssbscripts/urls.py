from django.urls import path
from . import views
app_name = "ssbscripts"
urlpatterns = [
    path('', views.index, name='home'),
    path('sharesmarthouse/', views.smarthouse, name='smarthouse'),
    path('test/', views.test, name='test'),
]



