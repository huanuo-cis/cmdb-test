
import os,django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cmdb_test.settings")
django.setup()

from assets.models import  Assets

with open('data.csv',encoding='utf-8') as file:
    for line in file:
        lst =line.strip().split(',')
        asset = Assets(asset_id=lst[0],asset_name=lst[1],asset_type=lst[2],asset_sn=lst[3],asset_manufacturer=lst[4],asset_mgmt_ip=lst[5],asset_hypervisor_type=lst[6])
        asset.save()

