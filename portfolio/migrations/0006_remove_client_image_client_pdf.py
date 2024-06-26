# Generated by Django 4.2.7 on 2024-06-25 17:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0005_contact"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="client",
            name="image",
        ),
        migrations.AddField(
            model_name="client",
            name="pdf",
            field=models.FileField(default="default.pdf", upload_to="Clients"),
        ),
    ]
