# Generated by Django 4.0.3 on 2022-03-20 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipt_generator_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='total_amount_payable',
            field=models.FloatField(),
        ),
    ]