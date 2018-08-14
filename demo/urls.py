
from django.urls import path
from . import views, hr_views, form_views, course_views

urlpatterns = [
    path('index/', views.index),
    path('discount/', views.discount),
    path('adddept/', hr_views.add_dept),
    path('listdept/', hr_views.list_dept),
    path('deletedept/', hr_views.delete_dept),
    path('countries/', views.list_countries),
    path('adddeptform/', form_views.add_dept),
    path('course_list/', course_views.list),
    path('course_add/', course_views.add),
]
