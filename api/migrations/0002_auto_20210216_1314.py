# Generated by Django 3.0.6 on 2021-02-16 10:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='status',
            field=models.BooleanField(default=1),
        ),
        migrations.AlterField(
            model_name='data',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]