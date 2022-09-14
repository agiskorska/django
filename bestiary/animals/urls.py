# Map view functions to URL patterns

from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="animals-home"),
    path("about/", views.about, name="animals-about"),
    path("show/<int:id>/", views.show, name="animals-show")
]