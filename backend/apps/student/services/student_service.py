from django.db import transaction
from ..models import Student


class StudentService:
    @staticmethod
    def list_students():
        return Student.objects.all()

    @staticmethod
    def get_student(pk):
        return Student.objects.get(pk=pk)

    @staticmethod
    @transaction.atomic
    def create_student(validated_data):
        return Student.objects.create(**validated_data)

    @staticmethod
    @transaction.atomic
    def update_student(student: Student, validated_data):
        for fields, value in validated_data.items():
            setattr(student, fields, value)
        student.save()
        return student
