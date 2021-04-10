# jobs_board_main/urls.py

from django.urls import path

# jobs_board_main/urls.py
from .views import get_jobs, get_job, subscribe, delete_job

urlpatterns = [
    # All jobs
    path('jobs/', get_jobs, name="jobs_view"),
    path('jobs/<int:id>', get_job, name="job_view"),
    path('jobs/<int:id>/subscribe', subscribe, name="subscribe_view"),
    path('jobs/<int:id>/delete', delete_job, name="delete_view"),
]
