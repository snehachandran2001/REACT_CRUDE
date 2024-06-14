"""
URL configuration for Crude project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from crudeApp  import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('allstudent', views.student_list, name='all_students'),
    path("student/<int:student_id>", views.student_by_id, name='student_by_id'),
    path('student_delete/<int:student_id>', views.student_delete_by_id, name='student_delete_by_id'),
    path('addstudent', views.student_create, name='add_student'),
    path('updatestudent/<int:student_id>', views.update_student, name='update_student'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
