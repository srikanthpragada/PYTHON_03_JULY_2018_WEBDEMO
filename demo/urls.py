
from django.urls import path
from . import views, hr_views

urlpatterns = [
    path('index/', views.index),
    path('discount/', views.discount),
    path('adddept/', hr_views.adddept),
]
