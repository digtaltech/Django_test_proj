# Generated by Django 3.0.6 on 2021-02-16 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.TextField(max_length=100)),
                ('fio', models.TextField(max_length=100)),
                ('balance', models.IntegerField()),
                ('hold', models.IntegerField()),
                ('status', models.TextField(max_length=500)),
            ],
        ),
    ]