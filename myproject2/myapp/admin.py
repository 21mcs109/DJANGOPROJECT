from django.contrib import admin
from .models import Member

# class MemberAdmin(admin.ModelAdmin):
#     list_display = ('firstname', 'middlename', 'lastname')

# admin.site.register(Member, MemberAdmin)
admin.site.register(Member)