# Generated by Django 4.1.3 on 2022-12-11 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quadshop', '0003_userprofile_zip'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OrderInfo',
        ),
    ]