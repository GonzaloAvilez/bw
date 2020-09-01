# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Slide


@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    readonly_fields = ('created_at', 'updated_at',)