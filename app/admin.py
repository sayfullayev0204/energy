from django.contrib import admin
from .models import Mahalla, EnergiyaSarfi

class EnergiyaSarfiInline(admin.TabularInline):
    model = EnergiyaSarfi
    extra = 1  # Qo'shimcha bo'sh maydon chiqadi

@admin.register(Mahalla)  # Mahalla modelini ro‘yxatdan o‘tkazyapmiz
class MahallaAdmin(admin.ModelAdmin):
    list_display = ("nomi", "manzil", "tashkil_qilgan_sana", "fuqaro_soni")
    inlines = [EnergiyaSarfiInline]  # Mahalla sahifasida EnergiyaSarfi chiqsin

@admin.register(EnergiyaSarfi)  # EnergiyaSarfi modelini ro‘yxatdan o‘tkazyapmiz
class EnergiyaSarfiAdmin(admin.ModelAdmin):
    list_display = ("mahalla", "oy", "yil", "elektr_kVt", "gaz_m3", "suv_m3", "qoʻshilgan_vaqt")
    list_filter = ("yil", "oy", "mahalla")
    search_fields = ("mahalla__nomi", "oy", "yil")
    ordering = ("-yil", "-oy")
    list_editable = ("elektr_kVt", "gaz_m3", "suv_m3")
    date_hierarchy = "qoʻshilgan_vaqt"
