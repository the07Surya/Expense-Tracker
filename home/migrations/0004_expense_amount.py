# Generated by Django 5.0.6 on 2024-07-06 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_profile_expenses'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='amount',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]