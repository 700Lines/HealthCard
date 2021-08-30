# Generated by Django 3.2.1 on 2021-08-15 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_signup', '0006_prescription'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='bdate',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='bdate',
        ),
        migrations.AddField(
            model_name='doctor',
            name='age',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='age',
            field=models.CharField(max_length=50, null=True),
        ),
    ]