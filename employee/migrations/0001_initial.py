# Generated by Django 4.1.5 on 2023-01-17 06:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Employee",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.CharField(blank=True, max_length=500)),
                ("position", models.CharField(max_length=100)),
                ("hiring_date", models.DateField()),
                ("leaves_count", models.IntegerField(default=0)),
                (
                    "employee",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="LeaveRequest",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("message", models.CharField(max_length=500)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("no_of_days", models.IntegerField(default=1)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("approved", "Approved"),
                            ("rejected", "Rejected"),
                            ("pending", "Pending"),
                        ],
                        max_length=10,
                    ),
                ),
                ("attachment", models.FileField(upload_to="uploads/% Y/% m/% d/")),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="leave_request",
                        to="employee.employee",
                    ),
                ),
            ],
        ),
    ]
