from django.contrib import admin
from .models import Post, Profile, Record
import csv
import datetime
from django.contrib import admin
from django.http import HttpResponse
from django.urls import reverse
from django.utils.safestring import mark_safe

admin.site.site_header = "MAVEN ADMIN"
admin.site.site_title = "MAVEN ADMIN"
admin.site.index_title = "Welcome from Admin Panel"

def export_to_csv(modeladmin, request, queryset): 
    opts = modeladmin.model._meta 
    response = HttpResponse(content_type='text/csv') 
    response['Content-Disposition'] = 'attachment;' \
        'filename={}.csv'.format(opts.verbose_name) 
    writer = csv.writer(response) 
     
    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many] 
    # Write a first row with header information 
    writer.writerow([field.verbose_name for field in fields]) 
    # Write data rows 
    for obj in queryset: 
        data_row = [] 
        for field in fields: 
            value = getattr(obj, field.name) 
            if isinstance(value, datetime.datetime): 
                value = value.strftime('%d/%m/%Y') 
            data_row.append(value) 
        writer.writerow(data_row) 
    return response 
export_to_csv.short_description = 'Export to CSV' 

class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'content_type', 'date']
	list_filter = ['content_type', 'date']
	actions = [export_to_csv]

class ProfileAdmin(admin.ModelAdmin):
	list_display = ['name', 'role', 'phone', 'email']
	actions = [export_to_csv]

class RecordAdmin(admin.ModelAdmin):
	list_display = ['name', 'intime', 'outtime', 'absent', 'date']
	list_filter = ['name', 'intime', 'outtime', 'absent', 'date']
	actions = [export_to_csv]

admin.site.register(Post, PostAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Record, RecordAdmin)