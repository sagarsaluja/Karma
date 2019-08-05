from django.views import generic
from faculty.models import courses,studentdata
from django.views.generic.edit import CreateView,UpdateView ,DeleteView
from django.http import HttpResponseRedirect , HttpResponse
from django.urls import reverse_lazy , reverse
from django.contrib.auth import authenticate , get_user_model ,login ,logout
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .forms import UserLoginForm ,UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from tablib import Dataset

def class_view_decorator(function_decorator):
    """Convert a function based decorator into a class based decorator usable
    on class based Views.

    Can't subclass the `View` as it breaks inheritance (super in particular),
    so we monkey-patch instead.
    """

    def simple_decorator(View):
        View.dispatch = method_decorator(function_decorator)(View.dispatch)
        return View

    return simple_decorator

def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "registration/login.html", context)

def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "registration/signup.html", context)

def logout_view(request):
    logout(request)
    return redirect('/faculty/login/')

@class_view_decorator(login_required)
class IndexView(generic.ListView):              #courses summary data
    template_name = 'faculty/index.html'

    def get_queryset(self):
        return courses.objects.all()

@class_view_decorator(login_required)
class Full_Student_Data(generic.ListView):      #full student data
    model=courses #what kind of object is to be created you will be able to access the attributes of this class in the template
    template_name = 'faculty/detail.html'

    def get_queryset(self):
        return studentdata.objects.all()

@class_view_decorator(login_required)
class Course_Student_Data(generic.DetailView): #3       #course specific data
    model=courses
    template_name = 'faculty/course_specific_detail.html'

@class_view_decorator(login_required)
class Edit_Karma_Home(generic.ListView):                #edit karma home (course list)
    template_name = 'faculty/editkarmahome.html'

    def get_queryset(self):
        return courses.objects.all()

@class_view_decorator(login_required)
class Edit_Karma_Course_Select(generic.DetailView):     #course specific detail in edit karma
    model = courses
    template_name = 'faculty/edit_karma.html'

@class_view_decorator(login_required)
class Student_Create(CreateView):                       #make a new student
    model = studentdata
    fields = ['centre','sid','sname','course']


@class_view_decorator(login_required)
class Student_Update(UpdateView):                       #update student detail
    model = studentdata
    fields = ['centre','sid','sname','course']

@class_view_decorator(login_required)                   #update karma of a selected student
class Edit(UpdateView):
    model = studentdata
    fields = ['activity_1','activity_2','activity_3','activity_4','activity_5','activity_6','activity_7','activity_8' ]


@class_view_decorator(login_required)
class Student_Delete(DeleteView):  # USE LATER IN ACTIVITIES
    model=studentdata
    success_url = reverse_lazy('faculty:edit-edit')


def simple_upload(request):
    if request.method == 'POST':
        student_data = studentdata()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read())
        result = studentdata.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            studentdata.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'core/simple_upload.html')

def user_manual(request):
    context = {''}
    return render(request , 'faculty/user_manual.html' , context)




















