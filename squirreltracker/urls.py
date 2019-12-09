"""squirreltracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
<<<<<<< HEAD
from django.urls import path,include
from squirrelapp import views
=======
from django.urls import include,path
>>>>>>> 72f79178000007576275080d607c1ca737fad5f6

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include ('squirrelapp.urls')),
    
]
