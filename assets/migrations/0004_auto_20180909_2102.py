# Generated by Django 2.0.1 on 2018-09-09 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0003_auto_20180909_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assets',
            name='asset_hypervisor_type',
            field=models.CharField(choices=[('physical_server', '物理机'), ('virtual_server', '虚拟机')], default='phcical_server', max_length=64, verbose_name='设备标签'),
        ),
    ]
