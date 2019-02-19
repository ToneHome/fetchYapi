from django.shortcuts import render

# Create your views here.



from django.http import FileResponse
from service.file  import shpFilesToZips,zip_path

def download(request,id):
    filePath = '/fetch/'+str(id) +r'/'
    filename = str(id)+'.zip'
    zipFile = zip_path(filePath,r'/fetch/',filename)
    file = open(zipFile, 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename='+filename+''
    return response


