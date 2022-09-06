# Generated by Django 4.1 on 2022-09-06 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Posting",
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
                ("title", models.CharField(max_length=20, verbose_name="제목")),
                ("content", models.CharField(max_length=200, verbose_name="본문")),
                ("password", models.CharField(max_length=255, verbose_name="비밀번호")),
                (
                    "dt_created",
                    models.DateTimeField(auto_now_add=True, verbose_name="생성일"),
                ),
                ("dt_updated", models.DateTimeField(auto_now=True, verbose_name="수정일")),
            ],
            options={
                "db_table": "posting",
            },
        ),
    ]
