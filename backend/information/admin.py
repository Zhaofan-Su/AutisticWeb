from django.contrib import admin
from information.models import Information, Content, SubTitle, SubContent, ListTitle, ListContent
# Register your models here.
admin.site.register(Information)
admin.site.register(Content)
admin.site.register(SubContent)
admin.site.register(SubTitle)
admin.site.register(ListContent)
admin.site.register(ListTitle)