from django.shortcuts import render, redirect
from django.views import View
from .models import *
from userapp.models import Sotuvchi


class BolimlarView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'bulimlar.html')
        return redirect('/')



class MahsulotlarView(View):
    def get(self, request):
        mahsulotlar=Mahsulot.objects.filter(sotuvchi__user=request.user)
        qidiruv_sozi=request.GET.get('soz')
        if qidiruv_sozi is not None:
            mahsulotlar = mahsulotlar.filter(nom__contains=qidiruv_sozi)|mahsulotlar.filter(brend__contains=
                                                                                      qidiruv_sozi)|mahsulotlar.filter(
                miqdor__contains=qidiruv_sozi)|mahsulotlar.filter(narx__contains=
                                                                        qidiruv_sozi)|mahsulotlar.filter(
                olchov__contains=qidiruv_sozi)

        data={
            'mahsulotlar': mahsulotlar
        }
        return render(request, 'products.html', data)

    def post(self, request):
        Mahsulot.objects.create(
            nom=request.POST.get('nom'),
            brend=request.POST.get('brand'),
            narx=request.POST.get('narx'),
            miqdor=request.POST.get('miqdor'),
            olchov=request.POST.get('olchov'),
            sotuvchi=Sotuvchi.objects.get(user=request.user)

        )
        return redirect('/bolimlar/mahsulotlar/')



class MijozlarView(View):
    def get(self, request):
        mijozlar=Mijoz.objects.filter(sotuvchi__user=request.user)
        qidiruv_sozi=request.GET.get('soz')
        if qidiruv_sozi is not None:
            mijozlar=mijozlar.filter(nom__contains=qidiruv_sozi)|mijozlar.filter(ism__contains=
            qidiruv_sozi)|mijozlar.filter(manzil__contains=qidiruv_sozi)|mijozlar.filter(tel__contains=
            qidiruv_sozi)|mijozlar.filter(qarz__contains=qidiruv_sozi)
        data={
            'mijozlar': mijozlar
        }
        return render(request, 'clients.html', data)

class ProductDeleteView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            a=Sotuvchi.objects.get(user=request.user)
            m=Mahsulot.objects.get(id=pk)
            if m.sotuvchi==a and request.user.is_staff:
                m.delete()
            return redirect('mahsulotlar')
        return redirect('login')



class PupdateView(View):
    def get(self, request, pk):
        hozirgi_ombor = Sotuvchi.objects.get(user=request.user)
        product = Mahsulot.objects.get(id=pk)
        if request.user.is_authenticated and hozirgi_ombor == product.sotuvchi:
            data = {
                'mahsulot':product
            }
            return render(request, 'product_update.html', data)
        else:
            return redirect('/bolimlar/mahsulotlar/')

    def post(self, request, pk):
        Mahsulot.objects.filter(id=pk).update(
            nom=request.POST.get('name'),
            brend=request.POST.get('brand_name'),
            narx=request.POST.get('price'),
            miqdor=request.POST.get('amount'),
            olchov=request.POST.get('olchov')
        )
        return redirect('/bolimlar/mahsulotlar/')

class MijozDeleteView(View):
    def get(self, request, son):
        if request.user.is_authenticated:
            sotuvchi=Sotuvchi.objects.get(user=request.user)
            mijoz=Mijoz.objects.get(id=son)
            if mijoz.sotuvchi==sotuvchi and request.user.is_staff:
                mijoz.delete()
            return redirect('/bolimlar/mijozlar/')
        return redirect('/')

class MijozUpdateView(View):
    def get(self, request, son):
        hozirgi_ombor = Sotuvchi.objects.get(user=request.user)
        mijoz=Mijoz.objects.get(id=son)
        if request.user.is_authenticated and hozirgi_ombor==mijoz.sotuvchi:
            data={
                'mijoz': mijoz
            }
            return render(request, 'client_update.html', data)
        return redirect('/bolimlar/mahsulotlar/')
    def post(self, request, son):
        Mijoz.objects.filter(id=son).update(
            ism=request.POST.get('ism'),
            nom=request.POST.get('nom'),
            tel=request.POST.get('tel'),
            manzil=request.POST.get('manzil'),
            qarz=request.POST.get('qarz')
        )
        return redirect('/bolimlar/mijozlar/')



