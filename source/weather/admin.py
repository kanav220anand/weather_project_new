from django.contrib import admin
from weather.models import SearchHistory


class SearchHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'keyword', 'created_at')
    search_fields = ['user__email', 'keyword']
    list_filter = ['found_result', 'keyword']


admin.site.register(SearchHistory, SearchHistoryAdmin)
