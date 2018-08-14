# Generated by Django 2.1 on 2018-08-14 11:15

from django.db import migrations, models
import localflavor.generic.models


class Migration(migrations.Migration):

    dependencies = [
        ('account_management', '0002_auto_20180814_0803'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankaccount',
            name='status',
            field=models.CharField(choices=[(1, 'Active'), (2, 'Suspended')], default=1, max_length=50),
        ),
        migrations.AlterField(
            model_name='bankaccount',
            name='iban',
            field=localflavor.generic.models.IBANField(include_countries=None, max_length=34, unique=True, use_nordea_extensions=False),
        ),
    ]