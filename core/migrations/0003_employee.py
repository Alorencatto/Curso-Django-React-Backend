# Generated by Django 3.1.7 on 2021-03-10 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_teste'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emplyee_regNo', models.TextField(unique=True)),
                ('emplyee_name', models.TextField()),
                ('employee_email', models.TextField()),
                ('employee_mobile', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]