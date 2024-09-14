from django.contrib import admin
from .models import Athlete
from unfold.contrib.import_export.forms import ExportForm, ImportForm
from import_export.admin import ImportExportModelAdmin
from unfold.admin import ModelAdmin

@admin.register(Athlete)
class AthleteAdmin(ModelAdmin, ImportExportModelAdmin):
    import_form_class = ImportForm
    export_form_class = ExportForm
    list_display = ('id', 'name', 'age', 'country', 'sport', 'gold_medals', 'silver_medals', 'bronze_medals', 'total_medals')
