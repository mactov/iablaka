from django.contrib import admin

from .models import Company, Project, Partner

admin.site.register(Company)
admin.site.register(Project)
admin.site.register(Partner)
