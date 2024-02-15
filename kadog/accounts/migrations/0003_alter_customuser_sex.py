# Generated by Django 5.0.1 on 2024-02-15 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='sex',
            field=models.CharField(choices=[('Male', 'male'), ('Female', 'female'), ('Other', 'other')], default='Male', max_length=10),
        ),
    ]