# Generated by Django 3.2.1 on 2021-08-15 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_signup', '0005_doctor_pharmacy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientName', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]