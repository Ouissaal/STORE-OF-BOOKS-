# Generated by Django 5.0.6 on 2024-06-12 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0007_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
