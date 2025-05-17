from django.urls import path, include
from .views import StudentDetailView, StudentListCreateView

urlpatterns = [
    path("students/", StudentListCreateView.as_view(), name="student"),
    path("students/<int:pk>/", StudentDetailView.as_view(), name="students-detail"),
]