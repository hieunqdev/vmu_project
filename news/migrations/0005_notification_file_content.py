# Generated by Django 4.1.2 on 2022-10-10 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_notification_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='file_content',
            field=models.FileField(null=True, upload_to='files'),
        ),
    ]
