from django.contrib import admin
from . models import NISFocalPoint,NISData,RightToInformation,GRS,EaseOfDoingBusiness,AuditedReport

# Register your models here.

admin.site.register(NISFocalPoint)
admin.site.register(NISData)
admin.site.register(RightToInformation)
admin.site.register(GRS)
admin.site.register(EaseOfDoingBusiness)
admin.site.register(AuditedReport)