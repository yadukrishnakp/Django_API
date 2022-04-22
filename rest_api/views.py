from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Employee
from .serializer import Employee_Serializer


# create new details
@api_view(['POST'])
def Create_Employee(request):
    serializer = Employee_Serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response("Employee added successfully")
