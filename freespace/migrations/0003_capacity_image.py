# Generated by Django 3.2.8 on 2021-11-05 16:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('freespace', '0002_auto_20211105_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='capacity',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images'),
            preserve_default=False,
        ),
    ]
