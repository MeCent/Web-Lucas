# Generated by Django 4.2.4 on 2023-09-23 21:20

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.png', upload_to='profiles/images/', validators=[users.models.validate_file_extension_photo]),
        ),
    ]
