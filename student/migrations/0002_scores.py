# Generated by Django 4.1.2 on 2022-10-12 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('training_programme', '0006_subjects_teacher'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scores_major_assignment', models.FloatField(blank=True, null=True)),
                ('scores_x', models.FloatField(blank=True, null=True)),
                ('scores_y', models.FloatField(blank=True, null=True)),
                ('scores_z', models.FloatField(blank=True, null=True)),
                ('grade', models.CharField(max_length=10)),
                ('studies_again', models.BooleanField()),
                ('exam_again', models.BooleanField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='training_programme.subjects')),
            ],
        ),
    ]
