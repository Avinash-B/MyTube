import os

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.static import serve


from all.forms import UploadForm
from transfers.filetransfers.api import prepare_upload, serve_file
from all.models import UploadModel


def index(request):
    all_files=UploadModel.objects.all()
    count=1
    pks=[]
    files=[]
    for each in all_files:
        pks.append(count)
        files.append(each)
        count+=1
    web_data = {'files': files, 'pks': pks}
    return render(request,'index_specific.html',context=web_data)

def docuploader(request):
    view_url = reverse('upload-handler')
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        form.save()
        return HttpResponseRedirect('/')

    upload_url, upload_data = prepare_upload(request, view_url)
    form = UploadForm()
    service="/all"
    return render(request, 'upload.html',
        {'form': form, 'upload_url': upload_url, 'upload_data': upload_data, 'service': service})

def docdownloader(request, pk):
    upload = get_object_or_404(UploadModel, pk=pk)
    return serve_file(request, upload.file)