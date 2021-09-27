from django.contrib import admin
from . models import SpecialPublicationReports,QuarterlyReport,AnnualReport

# Register your models here.
admin.site.register(SpecialPublicationReports)
admin.site.register(QuarterlyReport)
admin.site.register(AnnualReport)