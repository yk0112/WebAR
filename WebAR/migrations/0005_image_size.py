# Generated by Django 4.2 on 2023-07-21 14:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("WebAR", "0004_alter_image_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="image",
            name="size",
            field=models.IntegerField(default=1),
        ),
    ]
