"""steuervermeider URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.urls import path
from website import views


urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('berater/<int:question_number>/', views.berater, name='question'),
    path('berater/1/', views.berater, name='question'),
    #path('question/<int:question_number>/', views.question, name='question'),
    path('result/', views.result, name='result'),
    path('result_no/', views.result_no, name='result_no'),
    path('result_yes/', views.result_yes, name='result_yes'),
]
