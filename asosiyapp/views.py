from django.shortcuts import render, redirect
from django.views import View
from .models import *


class BolimlarView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'bulimlar.html')
        return redirect('/')

class MahsulotlarView(View):
    def get(self, request):
        if request.user.is_authenticated:

            data={
                'mahsulotlar': Mahsulot.objects.filter(sotuvchi__user=request.user)
            }
            return render(request, 'products.html', data)
        return redirect('/')

class MijozlarView(View):
    def get(self, request):
        if request.user.is_authenticated:
            data={
                'mijozlar': Mijoz.objects.filter(sotuvchi__user=request.user)
            }
            return render(request, 'clients.html', data)
        return redirect('/')

