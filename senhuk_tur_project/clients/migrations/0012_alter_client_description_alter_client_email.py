# Generated by Django 4.2.1 on 2023-07-04 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0011_alter_client_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='description',
            field=models.TextField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.TextField(max_length=100),
        ),
    ]
