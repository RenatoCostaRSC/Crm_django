from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path


app_name = 'core'
urlpatterns = [
    
    path('admin/', admin.site.urls),
]