from django.contrib.auth.models import User
from rest_framework import serializers

from employee.models import Employee, LeaveRequest

MAX_ALLOWED_LEAVES = 4
EMAIL_ID_EXISTING_MESSAGE = "Email ID already exist"
USER_NAME_EXISTING_MESSAGE = "Username already exist"
LEAVE_REQUEST_PENDING_MESSAGE = "Another leave request pending"
LEAVE_EXCEEDED_THE_LIMIT_MESSAGE = "Already availed permitted leaves"
MAX_LEAVES_COUNT_MESSAGE = f"Maximum {MAX_ALLOWED_LEAVES} leaves are allowed"


class EmployeeSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="employee.username")
    email = serializers.CharField(source="employee.email")

    class Meta:
        model = Employee
        fields = [
            "id",
            "name",
            "email",
            "description",
            "position",
            "hiring_date",
            "leaves_count",
        ]

    def create(self, validated_data):
        employee_data = validated_data.pop("employee")
        if User.objects.filter(email=employee_data["email"]).first():
            raise serializers.ValidationError(EMAIL_ID_EXISTING_MESSAGE)

        if User.objects.filter(email=employee_data["username"]).first():
            raise serializers.ValidationError(USER_NAME_EXISTING_MESSAGE)

        user = User.objects.create(**employee_data)
        employee = Employee.objects.create(employee=user, **validated_data)
        return employee


class LeaveRequestSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="employee.employee.username", read_only=True)
    email = serializers.CharField(source="employee.employee.email", read_only=True)

    class Meta:
        model = LeaveRequest
        fields = [
            "id",
            "name",
            "email",
            "message",
            "no_of_days",
            "start_date",
            "end_date",
            "attachment",
            "status",
        ]

    def create(self, validated_data):
        user = self.context.get("request", None).user.profile
        if LeaveRequest.objects.filter(employee=user, status="pending").first():
            raise serializers.ValidationError(LEAVE_REQUEST_PENDING_MESSAGE)
        if Employee.objects.filter(
            employee=user, leaves_count__gte=MAX_ALLOWED_LEAVES
        ).first():
            raise serializers.ValidationError(LEAVE_EXCEEDED_THE_LIMIT_MESSAGE)
        if validated_data["no_of_days"] > MAX_ALLOWED_LEAVES:
            raise serializers.ValidationError(MAX_LEAVES_COUNT_MESSAGE)
        leave_request = LeaveRequest.objects.create(employee=user, **validated_data)
        return leave_request

    def update(self, instance, validated_data):
        # Only admin can update the status
        user = self.context.get("request", None).user
        if not user.is_superuser and "status" in validated_data:
            validated_data.pop("status")

        if (
            validated_data["no_of_days"] > MAX_ALLOWED_LEAVES
            and "no_of_days" in validated_data
        ):
            raise serializers.ValidationError(MAX_LEAVES_COUNT_MESSAGE)
        instance.__dict__.update(validated_data)
        instance.save()

        return instance
