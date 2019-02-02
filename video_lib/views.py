from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.static import serve



import os


# Create your views here.
from transfers.filetransfers.backends.default import prepare_upload, serve_file
from video_lib.forms import UploadForm
from video_lib.models import UploadModel


def index(request):
    ls = os.getcwd() + "Videos/"
    count=1
    pks=[]
    files=[]
    for each in ls:
        pks.append(count)
        files.append(each)
        count+=1
    web_data = {'service_name': "Videos", 'files': files, 'pks': pks}
    return render(request,'index_specific.html',context=web_data)

def videouploader(request):
    view_url = reverse('upload-handler')
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        form.save()
        return HttpResponseRedirect('/')

    upload_url, upload_data = prepare_upload(request, view_url)
    form = UploadForm()
    return render(request, 'upload.html',
        {'form': form, 'upload_url': upload_url, 'upload_data': upload_data})

def videodownloader(request, pk):
    upload = get_object_or_404(UploadModel, pk=pk)
    return serve_file(request, upload.file)