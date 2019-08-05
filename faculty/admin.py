from django.contrib import admin
from faculty.models import courses, studentdata
from import_export import resources
from import_export.admin import ImportExportModelAdmin

admin.site.register(courses)



class StudentResource(resources.ModelResource):
    class Meta:
        model = studentdata

@admin.register(studentdata)
class studentdataAdmin(ImportExportModelAdmin):
    pass