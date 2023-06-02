from django.contrib import admin

from .models import Answer, Task, Test


class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'text',
        'level',
        'author'
    )
    search_fields = ('text',)
    list_filter = ('level', 'author')
    empty_value_display = '-пусто-'


class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'text',
        'point',
        'is_right',
        'task'
    )
    search_fields = ('text',)
    list_filter = ('point', 'is_right', 'task')
    empty_value_display = '-пусто-'


class TestAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'text',
        'author'
    )
    search_fields = ('title', 'text')
    list_filter = ('author',)
    empty_value_display = '-пусто-'


admin.site.register(Task, TaskAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Test, TestAdmin)
