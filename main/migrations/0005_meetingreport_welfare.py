# Generated by Django 4.2.9 on 2024-01-18 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0004_giving"),
    ]

    operations = [
        migrations.CreateModel(
            name="MeetingReport",
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
                ("date", models.DateField()),
                ("details", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Welfare",
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
                ("member_name", models.DateField()),
                ("details", models.TextField()),
                ("date", models.DateField(auto_now_add=True)),
            ],
        ),
    ]
