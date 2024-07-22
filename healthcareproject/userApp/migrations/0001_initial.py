# Generated by Django 4.2.13 on 2024-07-09 16:03

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
            name="Profile",
            fields=[
                ("profile_id", models.AutoField(primary_key=True, serialize=False)),
                ("address", models.CharField(blank=True, max_length=50, null=True)),
                ("phone", models.CharField(blank=True, max_length=11, null=True)),
                ("date_default_birth", models.DateField(max_length=11, null=True)),
                (
                    "gender",
                    models.CharField(
                        choices=[("Male", "Male"), ("Female", "Female")],
                        max_length=11,
                        null=True,
                    ),
                ),
                (
                    "nationality",
                    models.CharField(
                        choices=[
                            ("Nigeria", "Nigeria"),
                            ("Chana", "Chana"),
                            ("Unite Kindom", "UK"),
                            ("USA", "USA"),
                        ],
                        max_length=50,
                        null=True,
                    ),
                ),
                (
                    "state",
                    models.CharField(
                        choices=[
                            ("Abia", "Abia"),
                            ("Oyo", "Oyo"),
                            ("Osun", "Osun"),
                            ("Lagos", "Lagos"),
                            ("Kano", "Kano"),
                            ("Abuja", "Abuja"),
                        ],
                        max_length=20,
                        null=True,
                    ),
                ),
                (
                    "means_of_identity",
                    models.ImageField(null=True, upload_to="identityImage/"),
                ),
                (
                    "particulars",
                    models.FileField(null=True, upload_to="particularsImage/"),
                ),
                (
                    "profile_passport",
                    models.ImageField(null=True, upload_to="profileImage/"),
                ),
                (
                    "position",
                    models.CharField(
                        choices=[
                            ("Chairman", "Chairman"),
                            ("Director", "Director"),
                            ("Supervisor", "Supervisor"),
                            ("Admin", "Admin"),
                            ("Tour Agent", "Tour Agent"),
                            ("Maintenance", "Maintenance"),
                        ],
                        max_length=25,
                        null=True,
                    ),
                ),
                (
                    "marital_status",
                    models.CharField(
                        choices=[
                            ("Single", "Single"),
                            ("Married", "Married"),
                            ("Divorce", "Divorce"),
                            ("Complicate", "Complicate"),
                        ],
                        max_length=20,
                        null=True,
                    ),
                ),
                ("staff", models.BooleanField(default=False)),
                ("next_of_kin", models.CharField(max_length=20, null=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
