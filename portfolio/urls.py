from django.urls import path
from .views import IndexView, contact
from . import views

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("contact/", views.contact, name="contact")  # URL pattern for the IndexView
]
