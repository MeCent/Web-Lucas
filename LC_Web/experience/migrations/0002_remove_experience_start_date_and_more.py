# Generated by Django 4.2.4 on 2023-09-07 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experience',
            name='start_date',
        ),
        migrations.AlterField(
            model_name='experience',
            name='category',
            field=models.CharField(choices=[('Education', 'Education'), ('Course', 'Course'), ('Experience', 'Experience')], max_length=100),
        ),
    ]
