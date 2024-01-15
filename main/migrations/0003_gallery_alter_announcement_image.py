# Generated by Django 4.2.9 on 2024-01-15 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_announcement"),
    ]

    operations = [
        migrations.CreateModel(
            name="Gallery",
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
                ("image", models.ImageField(upload_to="gallery")),
                ("title", models.CharField(max_length=100)),
                ("body", models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name="announcement",
            name="image",
            field=models.ImageField(upload_to="announcement"),
        ),
    ]
