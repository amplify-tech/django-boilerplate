import pytest
from rest_framework import status
from rest_framework.test import APIClient
from apps.student.models import Student


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def student_data():
    return {
        "name": "ALpha 1",
        "email": "alpha.user@example.com",
        "dob": "2026-05-02",
        "grade": 2,
    }


@pytest.fixture
def create_student(student_data):
    student = Student.objects.create(**student_data)
    return student


@pytest.mark.django_db
def test_create_student(api_client, student_data):
    url = "/api/students/"
    response = api_client.post(url, student_data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["name"] == student_data["name"]


@pytest.mark.django_db
def test_get_student_list(api_client):
    url = "/api/students/"
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
