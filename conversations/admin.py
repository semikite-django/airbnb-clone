from django.contrib import admin

# Register your models here.
from . import models

@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created')


@admin.register(models.Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'count_messages', 'count_participants')
