
from django.urls import path
from . import views, hr_views, form_views, course_views, cookie_views, session_views
from . import class_views
from django.views.generic import TemplateView

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
    path('add_cookie/', cookie_views.add_cookie),
    path('list_cookies/', cookie_views.list_cookies),
    path('sessions/', session_views.add_key),
    path('list_keys/', session_views.list_keys),
    path('movies/', cookie_views.list_movies),
    path('selectcity/', cookie_views.select_city),
    path('savecity/', cookie_views.save_city),
    # path('classview1/', class_views.ClassView1.as_view()),
    path('classview1/', TemplateView.as_view( template_name = 'class_view1.html')),
    path('login/', class_views.LoginView.as_view()),
    path('courses/', class_views.ListCourseView.as_view()),

]
