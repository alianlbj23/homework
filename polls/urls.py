from . import views 
from django.urls import path
from django.contrib import admin
from polls.views import homepage, showpost

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('post/<slug:slug>/', showpost),
]
