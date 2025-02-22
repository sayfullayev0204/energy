from django.shortcuts import render, redirect
from .models import Mahalla, EnergiyaSarfi,Tavsiya
from .forms import EnergiyaSarfiForm
from django.http import HttpResponse,JsonResponse

def home(request):
    """Bosh sahifa - Oylik energiya grafiklarini ko‘rsatadi"""
    energiyalar = EnergiyaSarfi.objects.all()
    mahalla = Mahalla.objects.count()
    fuqaro = sum(Mahalla.objects.values_list('fuqaro_soni', flat=True))
    return render(request, 'home.html', {'energiyalar': energiyalar, 'mahalla':mahalla,'fuqaro':fuqaro})

def mahalla_list(request):
    """Mahallalar ro‘yxati"""
    mahallalar = Mahalla.objects.all()
    return render(request, 'mahalla_list.html', {'mahallalar': mahallalar})

def energiya_kiritish(request):
    """Yangi energiya sarfi ma’lumotini qo‘shish"""
    mahalla = Mahalla.objects.all()
    oylar = EnergiyaSarfi.objects.values_list('oy', flat=True)
    if request.method == "POST":
        form = EnergiyaSarfiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EnergiyaSarfiForm()
    return render(request, 'energiya_kiritish.html', {'form': form,'mahalla':mahalla})

def hisobot(request):
    """Hisobot sahifasi"""
    energiyalar = EnergiyaSarfi.objects.all()
    return render(request, 'hisobot.html', {'energiyalar': energiyalar})

def tavsiya(request):
    tavsiya = Tavsiya.objects.all()
    return render(request, 'tavsiya.html',{'tavsiya':tavsiya})


import openpyxl
from django.http import HttpResponse
from openpyxl.workbook import Workbook
from .models import EnergiyaSarfi

def eksport_excel(request):
    """Hisobotni Excel formatiga eksport qilish (pandas-siz)"""
    
    # **Yangi Excel fayl yaratish**
    wb = Workbook()
    ws = wb.active
    ws.title = "Energiya Hisoboti"
    
    # **Sarlavhalarni qo‘shish**
    headers = ["Mahalla", "Oy", "Yil", "Elektr (kVt)", "Gaz (m³)", "Suv (m³)", "Qo‘shilgan vaqt"]
    ws.append(headers)
    
    # **Ma'lumotlarni qo‘shish**
    energiyalar = EnergiyaSarfi.objects.all()
    for e in energiyalar:
        ws.append([
            e.mahalla.nomi, e.oy, e.yil, 
            e.elektr_kVt, e.gaz_m3, e.suv_m3, 
            e.qoʻshilgan_vaqt.strftime("%Y-%m-%d %H:%M")
        ])
    
    # **Faylni HTTP javob sifatida qaytarish**
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="hisobot.xlsx"'
    
    wb.save(response)
    return response

def statistik_data(request):
    """Oylik gaz, suv va elektr sarfi bo‘yicha ma'lumotlarni JSON shaklida chiqarish"""
    energiyalar = EnergiyaSarfi.objects.values("oy").order_by("yil")

    oylar = ['Yanvar', 'Fevral', 'Mart', 'Aprel', 'May', 'Iyun', 
             'Iyul', 'Avgust', 'Sentabr', 'Oktabr', 'Noyabr', 'Dekabr']
    
    data = {oy: {'elektr': 0, 'gaz': 0, 'suv': 0} for oy in oylar}

    for e in EnergiyaSarfi.objects.all():
        data[e.oy]['elektr'] += e.elektr_kVt
        data[e.oy]['gaz'] += e.gaz_m3
        data[e.oy]['suv'] += e.suv_m3

    return JsonResponse({
        "labels": oylar,
        "elektr": [data[oy]['elektr'] for oy in oylar],
        "gaz": [data[oy]['gaz'] for oy in oylar],
        "suv": [data[oy]['suv'] for oy in oylar],
    })
