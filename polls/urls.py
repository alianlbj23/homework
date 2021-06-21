from . import views 
from django.urls import path
from django.contrib import admin
from polls.views import index, showpost, home, population_chart

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('charttest/', home),
    path('post/<int:id>/', showpost),
    path('population-chart/', population_chart, name='population-chart'),
]
