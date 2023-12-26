"""
URL configuration for app project.

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
from django.conf import settings  # para uso de imagens
from django.conf.urls.static import static  # para uso de imagens
from django.contrib import admin
from django.urls import path

from cars.views import (
    CarsListView,
    NewCarCreateView,
    CarDetailView,
    CarUpdateView,
    CarDeleteView,
)
from accounts.views import register_view, login_view, logout_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    # path("cars/", cars_view, name="cars_list"),  #function based view
    # path("cars/", CarsView.as_view(), name="cars_list"),  # class based view
    path("cars/", CarsListView.as_view(), name="cars_list"),  # class generic view
    # path("new_car/", new_car_view, name="new_car"),  #function based view
    # path("new_car/", NewCarView.as_view(), name="new_car"), # class based view
    path("new_car/", NewCarCreateView.as_view(), name="new_car"),  # class generic view
    path(
        "car/<int:pk>/", CarDetailView.as_view(), name="car_detail"
    ),  # class generic view
    path(
        "car/<int:pk>/update/", CarUpdateView.as_view(), name="car_update"
    ),  # class generic view
    path(
        "car/<int:pk>/delete/", CarDeleteView.as_view(), name="car_delete"
    ),  # class generic view
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)  # para uso de imagens
