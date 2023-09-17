# Generated by Django 4.2.4 on 2023-09-17 12:06

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Subscriber",
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
                ("email", models.EmailField(max_length=100, unique=True)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "get_latest_by": "-timestamp",
            },
        ),
    ]