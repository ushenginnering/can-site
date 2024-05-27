# Generated by Django 4.2.9 on 2024-03-08 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_remove_gallery_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='action_text',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='announcement',
            name='action_url',
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
    ]