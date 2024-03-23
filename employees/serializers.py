from rest_framework import serializers
from employees.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=Employee
        fields="__all__"