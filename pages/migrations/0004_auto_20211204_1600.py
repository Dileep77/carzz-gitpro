# Generated by Django 3.0.7 on 2021-12-04 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20211204_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='photo',
            field=models.ImageField(upload_to='media/photos/%Y/%m/%d/'),
        ),
    ]
