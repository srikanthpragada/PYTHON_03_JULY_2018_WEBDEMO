
from django.urls import path
from . import views, hr_views

urlpatterns = [
    path('index/', views.index),
    path('discount/', views.discount),
    path('adddept/', hr_views.add_dept),
    path('listdept/', hr_views.list_dept),
    path('deletedept/', hr_views.delete_dept),
    path('countries/', views.list_countries),
]
