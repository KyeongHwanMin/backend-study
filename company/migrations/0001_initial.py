# Generated by Django 4.0.10 on 2023-10-11 04:46

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Company",
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
                ("name", models.CharField(help_text="회사명", max_length=255)),
                ("nation", models.CharField(help_text="국가", max_length=128)),
                ("area", models.CharField(help_text="지역", max_length=255)),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, help_text="생성 날짜"),
                ),
                ("modified_at", models.DateTimeField(auto_now=True, help_text="수정 날짜")),
            ],
            options={
                "db_table": "company",
            },
        ),
    ]
