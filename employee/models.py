from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class Employee(models.Model):

    employee = models.OneToOneField(User, related_name='profile',on_delete=models.CASCADE)
    description = models.CharField(max_length=500, blank=True)
    position = models.CharField(max_length=100)
    hiring_date = models.DateField()
    leaves_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.employee.username} - {self.leaves_count}"

@receiver(post_save, sender=Employee)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance.employee)
    
class LeaveRequest(models.Model):
    STATUS_CHOICES = (
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('pending', 'Pending'),
    )
    
    employee = models.ForeignKey(Employee,related_name="leave_request", on_delete=models.CASCADE)
    message = models.CharField(max_length=500)
    start_date = models.DateField()
    end_date = models.DateField()
    no_of_days = models.IntegerField(default=1)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")
    attachment = models.FileField(upload_to ='uploads/%Y/%m/%d/', null=True, blank=True)
    
    def __str__(self):
        return f"{self.employee.employee.username} - {self.status}"
    
    