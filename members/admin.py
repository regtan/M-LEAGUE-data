from django.contrib import admin
from .models import Member, Organization

admin.site.register(Organization)
admin.site.register(Member)