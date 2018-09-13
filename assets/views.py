from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView,TemplateView,CreateView

from assets.models import *

from assets.form import AssetForm

class AllAssets(ListView):
    template_name = 'assets/assets_list.html'
    model = Assets
    """等同queryset= = Assets.objects.all()"""
    context_object_name = 'assets_list'
    """默认变量名为object_list"""

#    def get_queryset(self):
        ##assets_list = Assets.objects.all()
#        return self.assets_list

class Dashboard(TemplateView):
    template_name = 'assets/dashboard.html'

class AddAssets(CreateView):
    template_name = 'assets/addassets.html'
    model = Assets
#    form_class = AssetForm
    success_url = 'assets/assets_list.html'
#    fields = ['asset_id','asset_name','asset_type','asset_sn','asset_manufacturer','mgmt_ip','asset_hypervisor_type']
"""
class AddAssets(CreateView):

    def get(self,request):
        return render(request,'assets/addassets.html')

    def post(self, request, *args, **kwargs):
        form = AddAssetForm(request.post)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('assets_list')
"""
def testpage(request):
    return HttpResponse("Test Page!")

def detail(request,asset_id):
    return HttpResponse("Server Name is %s." % asset_id)

def addTest(request):
    print(request.POST.get("inputassetid"))
    return HttpResponse("1")



def index(request):
    all_assets = Assets.objects.all()
    return render(request, 'assets/assets.html')