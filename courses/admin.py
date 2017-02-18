from django.contrib import admin
from .models import Subject, Course

# Register your models here.

class SubjectAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title", )}

admin.site.register(Subject)
admin.site.register(Course)

