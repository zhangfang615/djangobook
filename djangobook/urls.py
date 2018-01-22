"""djangobook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from Users.verificationViews import emailVerification, current_datetime, hours_ahead, display_meta, gettest, phoneRegister, emailRegister, userLogin
from django.conf.urls import url
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^emailVerification/([^/]+)/$', emailVerification),
    url(r'^display/$', display_meta),
    url('^time/$', current_datetime),
    url('^gettest/', gettest),
    url('^phoneRegister', phoneRegister),
    url('^emailRegister', emailRegister),
    url('^userLogin', userLogin),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
]
