# Generated by Django 4.1.3 on 2022-12-09 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quadshop', '0002_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='zip',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]