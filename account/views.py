from django.shortcuts import render
from django.http import JsonResponse
from django.views import View


class HelloView(View):

    def post(self, request):
        return JsonResponse(dict(hello='world'))

class MainView(View):

    def get(self, request):
        return JsonResponse(dict(hello='world'))
