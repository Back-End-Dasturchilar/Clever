from django.contrib import admin
from app.models import *
# Register your models here.
class CoursAdmin(admin.ModelAdmin):
    filter_horizontal = ['likes']
admin.site.register(Cours, CoursAdmin)
admin.site.register(Customer)
admin.site.register(Teacher)
admin.site.register(Category)
admin.site.register(Blog)