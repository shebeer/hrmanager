from employee.views import EmployeeViewSet, LeaveRequestViewSet
from rest_framework import routers

employee_router = routers.DefaultRouter()
employee_router.register(r"employees", EmployeeViewSet)
employee_router.register(r"leave-request", LeaveRequestViewSet)
