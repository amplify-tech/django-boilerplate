from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id", "name", "email", "dob", "grade", "enrolled_date"]
        read_only_fields = ("id", "enrolled_date")