# Generated by Django 5.1.4 on 2025-01-03 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employeeTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eNo', models.IntegerField()),
                ('eName', models.CharField(max_length=30)),
                ('eSal', models.FloatField()),
                ('eAdd', models.CharField(max_length=30)),
            ],
        ),
    ]