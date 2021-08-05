from django.contrib import admin
from .models import *

@admin.register(Normalization)
class NormalizationAdmin(admin.ModelAdmin):
    list_display = ['step', 'dataframe', 'note', 'error_message']

@admin.register(Column)
class ColumnAdmin(admin.ModelAdmin):
    list_display = ['algorithm', 'name']
