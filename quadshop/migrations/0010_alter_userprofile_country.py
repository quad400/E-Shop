# Generated by Django 4.1.3 on 2022-12-14 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quadshop', '0009_alter_userprofile_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='country',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
