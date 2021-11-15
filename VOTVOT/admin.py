from django.contrib import admin

from VOTVOT.models import Question, Answer

admin.site.register([
    Question,
    Answer,
])

admin.site.site_title = 'VOTVOT'
admin.site.site_header = 'VOTVOT'
admin.site.index_title = 'VOTVOT'