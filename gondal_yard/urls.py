from django.urls import path
from . import views

urlpatterns = [
    path('gondal-yard/', views.gondal_yard, name="gondal_yard"),
]
    
