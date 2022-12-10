from django.urls import path
from .views import *
from django.conf.urls import static
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
path('',index,name="home"),
path('register',register,name='reg'),
path('login',login,name='login')

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
