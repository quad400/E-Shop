# Generated by Django 4.1.3 on 2022-12-19 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quadshop', '0012_rename_color_id_variant_color_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='variant',
            name='image_id',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
