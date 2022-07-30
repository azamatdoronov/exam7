from django.contrib import admin

from webapp.models import Poll, Choice, Answer


class PollAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'created_p']
    list_display_links = ['question']
    list_filter = ['question']
    search_fields = ['question']
    fields = ['question', 'created_p', 'updated_p']
    readonly_fields = ['created_p', 'updated_p']


admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)
admin.site.register(Answer)
