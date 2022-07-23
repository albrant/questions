from django.contrib import admin

from .models import Option, Riddle


class RiddleOptionsInline(admin.TabularInline):
    model = Option
    extra = 1


@admin.register(Riddle)
class RiddleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'riddle_text', 'pub_date')
    ordering = ('pk',)
    empty_value_display = '-пусто-'
    list_editable = ('riddle_text',)
    inlines = [RiddleOptionsInline]


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'riddle', 'text', 'correct')
    ordering = ('pk',)
    empty_value_display = '-пусто-'
    list_editable = ('text',)
