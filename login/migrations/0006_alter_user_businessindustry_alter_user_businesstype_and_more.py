# Generated by Django 5.1.2 on 2024-11-01 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_remove_businessprofile_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='businessIndustry',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='businessType',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='gst_in',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='onlineShop',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
