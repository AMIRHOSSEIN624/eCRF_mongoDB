# Generated by Django 4.0.3 on 2022-08-18 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eCRF', '0005_patienthistory_datetime_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patienthistory',
            name='datetime_created',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='patienthistory',
            name='datetime_modified',
            field=models.DateTimeField(blank=True),
        ),
    ]
