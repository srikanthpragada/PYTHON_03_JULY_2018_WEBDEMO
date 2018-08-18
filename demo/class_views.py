from django.views.generic import TemplateView, ListView
from django.shortcuts import render
from .forms import LoginForm
from .models import Course


class ClassView1(TemplateView):
    template_name = 'class_view1.html'


class LoginView(TemplateView):
    template_name = 'login.html'

    def get(self, request):
        form = LoginForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['username'], form.cleaned_data['password'])

        return render(request, self.template_name, {'form': form})


# Generic View - ListView demo
class ListCourseView(ListView):
    model = Course
    template_name = "courses.html"    # default is  demo/course_list.html
    context_object_name = 'courses'   # default is  object_list
