from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from employees.models import Employee
from employees.serializers import EmployeeSerializer


class EmployeeViewset(ModelViewSet):
    serializer_class=EmployeeSerializer
    queryset=Employee.objects.all()
