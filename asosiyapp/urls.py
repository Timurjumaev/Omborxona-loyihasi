from django.urls import path
from .views import *

urlpatterns = [
    path('', BolimlarView.as_view(), name='bolimlar'),
    path('mahsulotlar/', MahsulotlarView.as_view(), name='mahsulotlar'),
    path('mijozlar/', MijozlarView.as_view(), name='mijozlar'),
    path('pr_delete/<int:pk>/', ProductDeleteView.as_view(), name='pr_delete'),
    path('mj_delete/<int:son>/', MijozDeleteView.as_view(), name='mj_delete'),
    path('pupdate/<int:pk>/', PupdateView.as_view(), name='pupdate'),
    path('mijozupdate/<int:son>/', MijozUpdateView.as_view(), name='mupdate'),

]