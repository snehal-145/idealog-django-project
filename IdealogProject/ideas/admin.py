from django.contrib import admin
from .models import Idea, CollaborationRequest

@admin.register(Idea)
class IdeaAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'status', 'created_at')
    search_fields = ('title', 'description', 'tags')


@admin.register(CollaborationRequest)
class CollaborationRequestAdmin(admin.ModelAdmin):
    list_display = ('idea', 'requester', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('idea__title', 'requester__username')

