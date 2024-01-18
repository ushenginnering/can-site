# Generated by Django 4.2.9 on 2024-01-18 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0006_alter_welfare_member_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="Publication",
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
                ("image", models.ImageField(upload_to="publication")),
                ("headline", models.CharField(max_length=100)),
                ("description", models.TextField()),
            ],
        ),
    ]
