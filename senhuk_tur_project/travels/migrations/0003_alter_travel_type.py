# Generated by Django 4.2.1 on 2023-07-04 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travels', '0002_rename_client_travel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travel',
            name='type',
            field=models.TextField(max_length=30),
        ),
    ]