# Generated by Django 4.2.2 on 2023-06-24 18:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="about_me",
            field=models.TextField(default="Admin of website"),
            preserve_default=False,
        ),
    ]