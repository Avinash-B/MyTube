import os

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from image_lib.forms import UploadForm
from image_lib.models import UploadModel
from transfers.filetransfers.api import prepare_upload, serve_file
from main import img_path


def index(request):
    ls=os.listdir(img_path)
    count=1
    pks=[]
    files=[]
    for each in ls:
        pks.append(count)
        files.append(each)
        count+=1
    web_data = {'service_name': "Images", 'path': img_path, 'files': files, 'pks': pks}
    return render(request,'index_specific.html',context=web_data)

def upload_handler(request):
    view_url = reverse('upload-handler')
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        form.save()
        return HttpResponseRedirect('/')

    upload_url, upload_data = prepare_upload(request, view_url)
    form = UploadForm()
    return render(request, 'upload.html',
        {'form': form, 'upload_url': upload_url, 'upload_data': upload_data})

def download_handler(request, pk):
    upload = get_object_or_404(UploadModel, pk=pk)
    return serve_file(request, upload.pk)