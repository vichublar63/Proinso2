"""
URL configuration for proinso_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from proinso_app import views

###urlpatterns = [
##    path('admin/', admin.site.urls),
##]

urlpatterns = [
        path('index/', views.index, name='index'),
    path('nuevo_cliente/', views.nuevo_cliente, name='nuevo_cliente'),
    path('nuevo_empleado/', views.nuevo_empleado, name='nuevo_empleado'),
    path('categoria/', views.categoria, name='categoria'),
    path('subcategoria/', views.subcategoria, name='subcategoria'),
    path('insumos/', views.insumos, name='insumos'),
    path('ventas/', views.ventas, name='ventas'),
    path('items/', views.items, name='items'),
###path("admin/", admin.site.urls),#foundation.urls
]