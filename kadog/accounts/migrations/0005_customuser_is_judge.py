# Generated by Django 5.0.1 on 2024-02-26 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_customuser_contact_number_alter_customuser_sex'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_judge',
            field=models.BooleanField(default=False),
        ),
    ]