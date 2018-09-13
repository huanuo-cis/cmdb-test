#-*- coding:UTF-8 -*-

from django.db import models

# Create your models here.

class Assets(models.Model):

    asset_type_choice = (
        ('server','服务器'),
        ('networkdevice', '网络设备'),
        ('storagedevice', '存储设备'),
        ('securitydevice', '安全设备'),
    )
    asset_hypervisor_choice = (
        ('physical_server','物理机'),
        ('virtual_server','虚拟机'),
    )

    asset_id = models.IntegerField(unique=True,verbose_name='资产ID')
    asset_name = models.CharField(default='unnamed',max_length=128,verbose_name='资产名称')
    asset_type = models.CharField(choices=asset_type_choice,max_length=64,default='server',verbose_name='资产类型')
    asset_sn = models.CharField(max_length=128,null='True', verbose_name='序列号')
    asset_manufacturer = models.CharField(max_length=128, null='True', verbose_name='生产商')
    mgmt_ip = models.GenericIPAddressField(verbose_name='管理IP',null='True')
    asset_hypervisor_type = models.CharField(choices=asset_hypervisor_choice,max_length=64,default='phcical_server',verbose_name='设备标签')

    def asset_with_z(self):
        pass

    def __str__(self):
        return self.asset_name


class Server(Assets):
    server_os = models.CharField(max_length=64)

    def __str__(self):
        return self.asset_name


class Network_device(Assets):
    device_os = models.CharField(max_length=64)

    def __str__(self):
        return self.asset_name
