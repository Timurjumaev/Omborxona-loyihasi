from django.shortcuts import render
from django.views import View

from statsapp.models import Statistika


class StatistikaView(View):
    def get(self, request):
        stats=Statistika.objects.filter(sotuvchi__user=request.user)
        qidiruv_sozi=request.GET.get('soz')
        if qidiruv_sozi is not None:
            stats=stats.filter(mahsulot__nom__contains=
            qidiruv_sozi)|stats.filter(mahsulot__brend__contains=
            qidiruv_sozi)|stats.filter(mijoz__nom__contains=
            qidiruv_sozi)|stats.filter(mijoz__ism__contains=qidiruv_sozi)

        data={
            'stats': stats
        }
        return render(request, 'stats.html', data)

