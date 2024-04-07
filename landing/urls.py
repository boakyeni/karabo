from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about-karabo-ai/", views.about, name="about"),
    path("karabo-pricing/", views.pricing, name="pricing"),
]
