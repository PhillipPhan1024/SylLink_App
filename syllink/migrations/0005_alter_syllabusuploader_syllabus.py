# Generated by Django 5.0.3 on 2024-03-29 20:11

import syllink.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("syllink", "0004_rename_syllabus_uploader_syllabusuploader"),
    ]

    operations = [
        migrations.AlterField(
            model_name="syllabusuploader",
            name="syllabus",
            field=models.FileField(upload_to=syllink.models.user_directory_path),
        ),
    ]
