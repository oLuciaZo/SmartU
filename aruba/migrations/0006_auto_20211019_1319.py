# Generated by Django 3.2.8 on 2021-10-19 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aruba', '0005_auto_20211019_1316'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Participant',
            new_name='Participants',
        ),
        migrations.RemoveField(
            model_name='switches',
            name='participant',
        ),
        migrations.AddField(
            model_name='switches',
            name='participants',
            field=models.ManyToManyField(blank=True, null=True, to='aruba.Participants'),
        ),
    ]
