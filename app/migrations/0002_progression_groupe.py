# Generated by Django 4.1.5 on 2023-01-30 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="progression",
            name="groupe",
            field=models.CharField(default="G2", max_length=2),
        ),
    ]
