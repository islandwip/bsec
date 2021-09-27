from django.contrib import admin
from . models import ChairmanMessage,AboutBsec,BsecMission,Commission,BsecFunction,Department,CommissionList,EmployeeList,AdvisoryCommittee,CitizenCharter
# Register your models here.


admin.site.register(ChairmanMessage)
admin.site.register(AboutBsec)
admin.site.register(BsecMission)
admin.site.register(Commission)
admin.site.register(BsecFunction)
admin.site.register(Department)
admin.site.register(CommissionList)
admin.site.register(EmployeeList)
admin.site.register(AdvisoryCommittee)
admin.site.register(CitizenCharter)