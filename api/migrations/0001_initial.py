# Generated by Django 4.2.11 on 2024-04-12 15:35

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
            name="Member",
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
                ("name", models.CharField(db_index=True, max_length=255)),
                ("dob", models.DateField()),
                ("hometown", models.CharField(max_length=255)),
                ("school", models.CharField(max_length=255)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Task",
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
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                (
                    "status",
                    models.SmallIntegerField(
                        choices=[
                            ("Not Started", "Not Started"),
                            ("In Progress", "In Progress"),
                            ("Completed", "Completed"),
                        ],
                        default="Not Started",
                    ),
                ),
                (
                    "assigned_to",
                    models.ManyToManyField(
                        blank=True,
                        db_index=True,
                        related_name="assigned_tasks",
                        to="api.member",
                    ),
                ),
            ],
        ),
    ]