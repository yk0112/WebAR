# Generated by Django 4.2 on 2023-05-21 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebAR', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='nickname',
            field=models.CharField(default='abc', max_length=30),
        ),
    ]
