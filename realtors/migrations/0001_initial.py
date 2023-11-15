# Generated by Django 3.0.5 on 2020-05-01 14:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Realtor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='photo/%Y/%m/%d/')),
                ('description', models.TextField(blank=True)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('is_mvp', models.BooleanField(default=False)),
                ('hire_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]