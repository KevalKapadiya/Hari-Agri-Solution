from django.urls import path
from . import views

urlpatterns = [
    path('find-work/', views.find_work, name="find_work"),
]
    
