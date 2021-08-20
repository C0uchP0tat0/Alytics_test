from django.contrib import admin
from .models import FunctionModel
from .figures import return_graph

class FunctionModelAdmin(admin.ModelAdmin):
    list_display = ('function', 'function_plot', 'interval', 'processing_date')

admin.site.register(FunctionModel, FunctionModelAdmin)
