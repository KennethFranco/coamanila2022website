from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home, name = "home"),
    path("about", views.about, name = "about"),
    path("organizations", views.organizations, name = "organizations"),
    path("indivorg/<int:pk>/", views.indivorg, name = "indivorg"),
    path("newsletters", views.newsletters, name = "newsletters"),
    path("indivnewsletter/<int:pk>/", views.indivnewsletter, name = "indivnewsletter"),
    path("articlepost", views.articlepost, name = "articlepost"),
    path("contactUs", views.contactUs, name = "contactUs"),
    path("services", views.services, name = "services"),
]