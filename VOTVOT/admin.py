from django.contrib import admin

from VOTVOT.models import Question, Option, Vote

admin.site.register([
    Question,
    Option,
    Vote,
])

admin.site.site_title = 'VOTVOT'
admin.site.site_header = 'VOTVOT'
admin.site.index_title = 'VOTVOT'