from django import forms
from assets.models import Assets

class AssetForm(forms.ModelForm):

    class Meta:
        model = Assets
        field = ['asset_id','asset_name','asset_type','asset_sn','asset_manufacturer','asset_mgmt_ip','asset_hypervisor_type']
        help_texts = {
            'asset_id':'* 必填内容，数字 ',
        }
