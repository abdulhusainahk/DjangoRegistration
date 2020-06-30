"""abcd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from tem import views
from tem.views import GeneratePdf

app_name = "xc"

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', views.emp),
	path('show', views.show),
	path('home', views.home),
	path('access', views.access_session),
	path('delete', views.delete_session),
	path('loginpage', views.loginpage),
	path('pdf/', views.GeneratePdf.as_view()),
	path('blog', views.blog),
	path('course', views.course),
	path('dbms', views.dbms),
	path('os', views.os),
	path('hci', views.hci),
	path('toc', views.toc),
	path('sepm', views.sepm),
	path('contact', views.contact),
	path('pricing', views.pricing),
	path('index1', views.index1),
	path('dm', views.dm),
	path('courses1', views.courses1),
	path('mapping', views.mapping),
	path('ind', views.ind),
	path('indi', views.indi),
	path('result', views.result),
	path('display2', views.display2),
	path('adminentry', views.adminentry),
	path('adminlogin', views.adminlogin),
	path('adminhomepage', views.adminhomepage),
	path('coursescheme', views.coursescheme),
	path('result', views.result),
	path('display2', views.display2),
	path('weights', views.weights),
	path('teacherentry', views.teacherentry),
	path('teacher_alloc', views.teacher_alloc),
	path('report_gen', views.report_gen),
	path('showreport', views.showreport),
	path('poentry', views.poentry),
	path('courseinfo', views.courseinfo),
	path('programs',views.programs),
	path('gencis',views.gencis)
]
