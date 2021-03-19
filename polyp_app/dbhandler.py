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

class Get:
    def dataset(self):
        return DatasetTable.objects.all()
