# Generated by Django 5.0.6 on 2024-06-10 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0004_delete_orderdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='book_image/'),
        ),
    ]
