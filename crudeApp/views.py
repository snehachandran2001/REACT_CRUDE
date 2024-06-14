from .serializer import StudentSerializer
from .models import StudentModel
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def student_list(request):

    students = StudentModel.objects.all()
    student_serializer_obj =StudentSerializer(students, many=True)
    return Response(student_serializer_obj.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def student_by_id(request, student_id):

    try:
        student_obj = StudentModel.objects.get(student_id=student_id)
        student_serializer_obj = StudentSerializer(student_obj, many=False)
        return Response(student_serializer_obj.data, status=status.HTTP_200_OK)
    except StudentModel.DoesNotExist:
        return Response({'message': "student not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(["DELETE"])
def student_delete_by_id(request, student_id):

    try:
        student_obj = StudentModel.objects.get(student_id=student_id)
        student_obj.delete()
        return Response({"message": "Student deleted successfully"}, status=status.HTTP_200_OK)
    except StudentModel.DoesNotExist:
        return Response({'message': "Student not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
def student_create(request):

    student_serializer_obj = StudentSerializer(data=request.data)
    if student_serializer_obj.is_valid():
        student_serializer_obj.save()
        return Response(student_serializer_obj.data, status=status.HTTP_201_CREATED)
    return Response(student_serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_student(request, student_id):

    try:
        student_obj = StudentModel.objects.get(student_id=student_id)
        student_serializer_obj = StudentSerializer(instance=student_obj, data=request.data, partial=True)
        if student_serializer_obj.is_valid():
            student_serializer_obj.save()
            return Response(student_serializer_obj.data, status=status.HTTP_200_OK)
        return Response(student_serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)
    except StudentModel.DoesNotExist:
        return Response({'message': "Book not found"}, status=status.HTTP_404_NOT_FOUND)