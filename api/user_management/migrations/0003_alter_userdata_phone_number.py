# Generated by Django 5.1.4 on 2025-01-03 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0002_alter_userdata_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
