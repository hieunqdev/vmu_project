# Generated by Django 4.1.2 on 2022-10-12 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training_programme', '0006_subjects_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjects',
            name='school_year',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='subjects',
            name='term',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
