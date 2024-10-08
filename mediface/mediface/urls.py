"""
URL configuration for mediface project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from django.http import HttpResponseRedirect
from diagnosis import views  # diagnosisアプリのビューをインポート

urlpatterns = [
    path('admin/', admin.site.urls),
    path('diagnose/', views.chat_diagnose_view, name='diagnose'),
    path('', lambda request: HttpResponseRedirect('/diagnose/')),
    path("mapapi/", views.mapapi_view, name="mapapi"),
    path("question/", views.question_diagnose_view, name="question"),
    # 他のURLパターンもここに追加できます
]
