from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Bosh sahifa (grafiklar)
    path('mahallalar/', views.mahalla_list, name='mahalla_list'),  # Mahallalar ro‘yxati
    path('energiya/kiritish/', views.energiya_kiritish, name='energiya_kiritish'),  # Yangi energiya sarfini qo‘shish
    path('hisobot/', views.hisobot, name='hisobot'),  # Hisobotlar
    path('hisobot/export/', views.eksport_excel, name='eksport_excel'),
    path('hisobot/statistik/', views.statistik_data, name='statistik_data'),
]
