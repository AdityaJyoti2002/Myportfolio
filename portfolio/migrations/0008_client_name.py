# Generated by Django 4.2.7 on 2024-06-25 18:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0007_remove_client_date_remove_client_description_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="client",
            name="name",
            field=models.CharField(max_length=100, null=True),
        ),
    ]
