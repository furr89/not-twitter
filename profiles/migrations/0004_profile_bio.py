# Generated by Django 4.1.5 on 2023-01-24 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]
