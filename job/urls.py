"""URL mapping for job App."""

from django.urls import path

from job import views

urlpatterns = [
    path('', views.index),
    path('<int:pk>', views.job_detail),
    path('newsletter', views.job_newsletter),
]
