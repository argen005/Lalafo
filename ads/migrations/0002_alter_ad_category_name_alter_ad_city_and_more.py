# Generated by Django 4.2.5 on 2024-01-09 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='category_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='ad',
            name='city',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='ad',
            name='phone_number',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='ad',
            name='price',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='ad',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='ad',
            name='user',
            field=models.CharField(max_length=255),
        ),
    ]
