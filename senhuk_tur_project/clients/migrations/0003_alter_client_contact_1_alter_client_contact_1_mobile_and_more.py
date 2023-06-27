# Generated by Django 4.2.1 on 2023-06-27 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_alter_client_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='contact_1',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='contact_1_mobile',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='contact_2',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='contact_2_mobile',
            field=models.IntegerField(null=True),
        ),
    ]
