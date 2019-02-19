from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from service.fetchWebSite import CheckUrlJurisdiction
import  os
from service.file import mkdir
import json

@api_view(http_method_names=['POST'])
def fetchApi(request):
    search = get_SearchObject(request)
    # search.geturlpath()
    result = {}
    result['msg'] = '1'
    result['list'] = search.get_api_cat()
    return Response(result)

@api_view(http_method_names=['POST'])
def getApiTree(request):
    search = get_SearchObject(request)
    cat_list = request.data['catList']
    result = {}
    result['msg'] = '1'
    result['list'] = search.get_api_tree(cat_list)
    return Response(result)

@api_view(http_method_names=['POST'])
def download(request):
    from apiApp.models import ApiName
    apiProjectId = request.data['apiProjectId']
    filePath = '/fetch/' + str(apiProjectId)
    mkdir(filePath, '')

    apTree = request.data['apTree']

    indexContent = ""
    indexExport = ""
    for item in apTree:
        ary = []
        file_name = item['file_name']
        child = item['child']
        catId = item['cat_id']
        indexContent = indexContent + "import " + file_name + " from './"+ file_name +"'; " ;
        indexExport = indexExport + file_name + ","
        for childItem in child:
            ApiName.objects.filter(ProjectId=apiProjectId, CarId=catId, ApiId=childItem['_id']).delete()
            ApiName.objects.create(ProjectId=apiProjectId, CarId=catId, ApiId=childItem['_id'],ApiName=childItem['title_english'])
            oneChild = {}
            oneChild["name"] = childItem['title_english']
            oneChild["method"] = childItem['method']
            oneChild["desc"] = u''+ childItem['title']
            oneChild["path"] = childItem['path']
            oneChild["params"] = {}
            ary.append(oneChild)

        strs = "export default "+json.dumps(ary, ensure_ascii=False)
        thisPath = filePath + '/' + file_name + '.js'
        mkdir(thisPath, strs)

    indexContent = indexContent + " export default { " + indexExport.strip(',') + " } "
    indexJsPath = filePath + '/index.js'
    mkdir(indexJsPath, indexContent)
    result = {}
    result['msg'] = '1'
    return Response(result)

def get_SearchObject(request):
    apiBaseUrl = request.data['apiBaseUrl']
    apiProjectId = request.data['apiProjectId']
    username = request.data['username']
    password = request.data['password']
    return CheckUrlJurisdiction(username,password,apiProjectId,apiBaseUrl)
