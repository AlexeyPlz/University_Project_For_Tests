from django.contrib import admin

from .models import Answer, Result, ResultAnswer, Task, Test


@admin.register(Task)
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


@admin.register(Answer)
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


@admin.register(Test)
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


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'points',
        'date',
        'test',
        'student'
    )
    search_fields = ('points', 'test', 'student')
    list_filter = ('student',)
    empty_value_display = '-пусто-'


@admin.register(ResultAnswer)
class ResultAnswerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'answer',
        'result'
    )
    empty_value_display = '-пусто-'
