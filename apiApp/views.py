from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from service.fetchWebSite import CheckUrlJurisdiction

@api_view(http_method_names=['POST'])
def fetchApi(request):
    apiBaseUrl = request.data['apiBaseUrl']
    apiProjectId = request.data['apiProjectId']
    username = request.data['username']
    password = request.data['password']
    search = CheckUrlJurisdiction(username,password,apiProjectId,apiBaseUrl)
    search.geturlpath()
    result = {}
    result['msg'] = '123'
    return  Response(result)