# Generated by Django 2.0.1 on 2018-09-09 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0002_assets_asset_hypervisor_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assets',
            name='asset_sn',
            field=models.CharField(max_length=128, verbose_name='序列号'),
        ),
    ]