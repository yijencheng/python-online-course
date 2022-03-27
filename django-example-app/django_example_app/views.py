from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt



# @csrf_exempt
def test(request):
    return JsonResponse({"status":'200', "message":"Success!"}, status=200)