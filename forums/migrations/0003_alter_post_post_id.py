# Generated by Django 4.2.2 on 2023-06-19 17:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("forums", "0002_post_post_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="post_id",
            field=models.PositiveIntegerField(),
        ),
    ]
