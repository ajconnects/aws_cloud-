# Generated by Django 5.0.4 on 2024-05-03 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("title", models.CharField(max_length=100)),
                ("text", models.TextField(max_length=2000)),
                ("date_create", models.DateTimeField(auto_now_add=True)),
                ("date_modified", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
