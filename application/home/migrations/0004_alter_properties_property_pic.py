# Generated by Django 4.1.5 on 2023-04-11 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_properties'),
    ]

    operations = [
        migrations.AlterField(
            model_name='properties',
            name='property_pic',
            field=models.FileField(upload_to='images/'),
        ),
    ]
