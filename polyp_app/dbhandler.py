from polyp_app.forms import *

class Insert:
    def dataset(self,data,files):
        res = False
        error = None
        form=DatasetTableForm(data,files)
        if form.is_valid():
            res = True
            form.save()
        if form.errors:
            error = form.errors
            print(form.errors)

        return res, error
    def detection(self,data,files):
        res = {}
        error = None
        form=DetectionTableForm(data,files)
        if form.is_valid():
            res["result"] = True
            m_detection = form.save()
            res["image_url"] = m_detection.image.url
        if form.errors:
            error = form.errors
            print(form.errors)

        return res, error

class Get:
    def dataset(self):
        return DatasetTable.objects.all()
