# Generated by Django 4.2.7 on 2024-06-23 18:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0004_recentwork_category_recentwork_link"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("name", models.CharField(max_length=100, verbose_name="Name")),
                ("Email", models.CharField(max_length=100, verbose_name="Email")),
                ("subject", models.CharField(max_length=100, verbose_name="Email")),
                ("message", models.TextField(null=True, verbose_name="message")),
            ],
        ),
    ]
