from django.contrib import admin

from resumeapp.models import Resume

# Register your models here.

class ResumeAdmin(admin.ModelAdmin):
    list_display=['name']



admin.site.register(Resume,ResumeAdmin)