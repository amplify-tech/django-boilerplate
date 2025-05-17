from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist

from .serializers import StudentSerializer
from .services.student_service import StudentService

class StudentListCreateView(APIView):
    def get(self, request):
        students = StudentService.list_students()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            student = StudentService.create_student(serializer.validated_data)
            return Response(StudentSerializer(student).data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class StudentDetailView(APIView):
    def get(self, request, pk):
        try:
            student = StudentService.get_student(pk)
        except ObjectDoesNotExist:
            return Response({"error": "Student not found"},
                            status.HTTP_404_NOT_FOUND
                    )
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    
    def post(self, request, pk):
        try:
            student = StudentService.get_student(pk)
        except ObjectDoesNotExist:
            return Response({"error": "Student not found"},
                            status.HTTP_404_NOT_FOUND
                    )
        
        serializer = StudentSerializer(instance=student, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        updated_student = StudentService.update_student(
            student,serializer.validated_data)
        return Response(StudentSerializer(updated_student).data)
    