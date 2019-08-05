from django.conf.urls import url
from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView
from faculty.views import login_view , register_view , logout_view , user_manual

app_name='faculty'
urlpatterns = [
    #/faculty/
    url(r'^$', views.IndexView.as_view(), name='index'),
    #/faculty/1/
    url(r'^(?P<pk>[0-9]+)/$',views.Full_Student_Data.as_view() ,name='detail'),

    #/faculty/login/
    url(r'login/', login_view ,name='login'),

    #/faculty/signup/
    url(r'signup/', register_view ,name='signup'),

    #/faculty/logout/
    url(r'logout/', logout_view ,name='logout'),

    #redirect after login
    url(r'/accounts/profile/' ,views.IndexView.as_view(), name='index'),

    #/faculty/fullstudentdata/
    url(r'fullstudentdata/',views.Full_Student_Data.as_view(),name='detail'),

    #/faculty/fullstudentdata/1
    url(r'^specific_studentdata/(?P<pk>[0-9]+)/$',views.Course_Student_Data.as_view() ,name='specific_detail'),

    # faculty/student/add/   #faculty/1
    url(r'studentadd/$', views.Student_Create.as_view(), name='student-add'), #2

    url(r'^studentadd/None$', views.Student_Create.as_view(), name='create'),  # 2 after submit button is pressed

    #faculty/studentupdate/    #faculty/2
    url(r'studentupdate/(?P<pk>[0-9]+)/$',views.Student_Update.as_view(), name='student-update'), #3

    # blueshit
    url(r'^studentupdate/(?P<pk>[0-9]+)/None$', views.Student_Update.as_view(), name='home'),  # 3

    # faculty/edit_karma_edit//2/   #faculty/3
    url(r'^edit_karma_edit/(?P<pk>[0-9]+)/$', views.Edit.as_view(), name='edit-edit'),#1 #clicking on edit button

    # blueshit
    url(r'^edit_karma_edit/(?P<pk>[0-9]+)/None$', views.Edit.as_view(), name='vow'),  # 1

    # faculty/editkarma_home/
    url(r'editkarma_home/', views.Edit_Karma_Home.as_view(), name='edit-home'), #edit karma nav button

    # faculty/edit_karma/2/
    url(r'^edit_karma/(?P<pk>[0-9]+)/$', views.Edit_Karma_Course_Select.as_view(), name='edit-karma-course_select'), #course select
    #faculty/editkarma/submit/3/






    url(r'^user_manual.html$' , user_manual , name='user_manual')


    ]

