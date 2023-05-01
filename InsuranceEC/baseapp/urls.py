from django.urls import path

from . import views

urlpatterns = [
    path("", views.starting_page, name="home-page"),
    path("/index", views.starting_page, name="starting-page"),
    path("/about", views.about, name="about-page"),
    path("/services", views.services, name="services-page")
]