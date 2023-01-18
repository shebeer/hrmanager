from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from employee.models import Employee, LeaveRequest
from rest_framework.response import Response

from employee.serializer import EmployeeSerializer, LeaveRequestSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('-hiring_date')
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]


class LeaveRequestViewSet(viewsets.ModelViewSet):
    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveRequestSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
    

