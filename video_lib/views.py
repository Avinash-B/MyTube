from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import urls

import main as paths


import os


# Create your views here.
from transfers.filetransfers.backends.default import prepare_upload, serve_file
from video_lib.forms import UploadForm
from video_lib.models import UploadModel


def index(request):
    ls=os.listdir(paths.video_path)
    files=[]
    for each in ls:
        files.append(each)
    web_data = {'service_name': "Videos", 'path': paths.video_path, 'files': files}
    return render(request,'index_specific.html',context=web_data)

def upload_handler(request):
    view_url = reverse('upload-handler')
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        form.save()
        return HttpResponseRedirect(view_url)

    upload_url, upload_data = prepare_upload(request, view_url)
    form = UploadForm()
    return render(request, 'upload.html',
        {'form': form, 'upload_url': upload_url, 'upload_data': upload_data})

def download_handler(request, pk):
    upload = get_object_or_404(UploadModel, pk=pk)
    return serve_file(request, upload.file)