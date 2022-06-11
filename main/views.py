from django.shortcuts import render
from rest_framework.decorators import api_view
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from rest_framework.response import Response
import requests

SEARCH_HOST = "https://api.stackexchange.com"
END_POINT = "/2.3/search/advanced"


@cache_page(60*60*1)
@vary_on_cookie
@api_view(['GET'])
def search(request):
    search_term = request.GET['q']
    page = request.GET['page']
    pagesize = request.GET['pagesize']
    query = "?q=%s&page=%s&pagesize=%s&site=stackoverflow" % (
        search_term, page, pagesize)
    response = requests.get(SEARCH_HOST+END_POINT+query)
    result = response.json()
    return Response(result)


def index(request):
    return render(request, 'index.html')
