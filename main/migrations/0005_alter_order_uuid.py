# Generated by Django 5.0.7 on 2024-07-10 16:35

import shortuuid.main
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_order_id_alter_order_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='uuid',
            field=models.CharField(default=shortuuid.main.ShortUUID.uuid, max_length=22, unique=True),
        ),
    ]