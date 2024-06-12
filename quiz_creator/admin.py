from django.contrib import admin
from .models import *

class HintAdmin(admin.ModelAdmin):
    list_display = ('question', 'hint_text', 'is_audio', 'hint_language', 'order')
    list_filter = ('question',)

admin.site.register(Question)
admin.site.register(Quiz)
# admin.site.register(QuizQuestion)
admin.site.register(Hint, HintAdmin)
admin.site.register(Language)