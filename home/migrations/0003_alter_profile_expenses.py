# Generated by Django 5.0.6 on 2024-07-06 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_profile_expenses_alter_profile_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='expenses',
            field=models.FloatField(default=0),
        ),
    ]