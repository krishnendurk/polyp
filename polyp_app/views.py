from django.shortcuts import render
from django.views.generic import View
from polyp_app import utils
from polyp_app import dbhandler

# Create your views here.
class DasboardView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, template_name="dashboard.html", context=context)   
    def post(self, request, *args, **kwargs):
        result = {}

        return render(request, template_name="dashboard.html", context = result)   

class AddDatasetView(View):
    def get(self, request, *args, **kwargs):
        
        context = {
            "classes":utils.CLASS_NAMES
        }
        return render(request, template_name="add_dataset.html", context=context)   
    def post(self, request, *args, **kwargs):
        data=request.POST
        print(data)
        result = {
            "class_name":data["class_name"]
        }

        return render(request, template_name="add_dataset_upload.html", context = result) 

# /polyp/upload_image/
class UploadDatasetView(View):
    def get(self, request, *args, **kwargs):
        
        context = {
            "classes":utils.CLASS_NAMES
        }
        return render(request, template_name="add_dataset.html", context=context)   
    def post(self, request, *args, **kwargs):
        data=request.POST
        files=request.FILES
        res, error = dbhandler.Insert().dataset(data,files)        
        result = {
            "class_name":data["class_name"],
            "result":res,
            "error" : error
        }

        return render(request, template_name="add_dataset_upload.html", context = result)  
# /polyp/view_all_image/
class ViewAllImage(View):
    def get(self, request, *args, **kwargs):
        m_dataset = dbhandler.Get().dataset()
        context = {   
            "m_dataset" :  m_dataset         
        }
        return render(request, template_name="view_all_image.html", context=context)   
    def post(self, request, *args, **kwargs):
        data=request.POST
        files=request.FILES
        res, error = dbhandler.Insert().dataset(data,files)        
        result = {
            "class_name":data["class_name"],
            "result":res,
            "error" : error
        }

        return render(request, template_name="view_all_image.html", context = result)  