# Generated by Django 2.2.4 on 2019-08-15 16:02

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('place', models.CharField(max_length=100, null=True)),
                ('address', models.TextField(max_length=200, null=True)),
                ('initialDate', models.DateField(default=datetime.date.today)),
                ('finalDate', models.DateField(default=datetime.date.today)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
