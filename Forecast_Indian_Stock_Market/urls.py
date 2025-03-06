"""diabetic_walking_through URL Configuration

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
from admins import views as admins
from django.urls import path
from users import views as usr
from . import views as mainView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', mainView.index, name='index'),
    path("UserRegister/", mainView.UserRegister, name="UserRegister"),
    path("AdminLogin/", mainView.AdminLogin, name="AdminLogin"),
    path('index/', mainView.index, name='index'),
    path("UserLogin/", mainView.UserLogin, name="UserLogin"),

    ### User Side Views
    path("UserRegisterActions/", usr.UserRegisterActions, name="UserRegisterActions"),
    path("UserLoginCheck/", usr.UserLoginCheck, name="UserLoginCheck"),
    path("UserHome/", usr.UserHome, name="UserHome"),
    path("user_view_data/", usr.user_view_data, name="user_view_data"),
    path("user_trainset/", usr.user_trainset, name="user_trainset"),
    path("user_testset/", usr.user_testset, name="user_testset"),
    path("user_prediction/", usr.user_prediction, name="user_prediction"),
    path("user_train_deep_learning/", usr.user_train_deep_learning, name="user_train_deep_learning"),
    path("analysis/", usr.analysis, name="analysis"),
    ### Admin Side Views
    path("AdminLoginCheck/", admins.AdminLoginCheck, name="AdminLoginCheck"),
    path("AdminHome/", admins.AdminHome, name="AdminHome"),
    path("ViewRegisteredUsers/", admins.ViewRegisteredUsers, name="ViewRegisteredUsers"),
    path("admin_forecast/", admins.admin_forecast, name="admin_forecast"),
    path("AdminActivaUsers/", admins.AdminActivaUsers, name="AdminActivaUsers"),

    # path("AdminDataPreProcess/", admins.AdminDataPreProcess, name="AdminDataPreProcess"),
]
