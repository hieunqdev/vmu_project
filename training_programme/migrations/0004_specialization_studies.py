# Generated by Django 4.1.2 on 2022-10-11 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training_programme', '0003_alter_department_head_of_department_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialization',
            name='studies',
            field=models.CharField(max_length=50, null=True),
        ),
    ]