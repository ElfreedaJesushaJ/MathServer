from django.contrib import admin 
from django.urls import path 
from resistor import views 
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('powerlamp/',views.powerlamp,name="powerlamp"),
    path('',views.powerlamp,name="powerlamp")
]