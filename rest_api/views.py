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


# show all employees details
@api_view(['GET'])
def Show_all_Employees(request):
    employees = Employee.objects.all()
    serializer = Employee_Serializer(employees, many=True)
    return Response(serializer.data)


# show one employee details
@api_view(['GET'])
def Show_Employee(request, pk):
    employees = Employee.objects.get(id=pk)
    serializer = Employee_Serializer(employees, many=False)
    return Response(serializer.data)
