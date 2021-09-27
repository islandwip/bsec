from django.contrib import admin
from . models import TrainingNotice,InvestorEduProgram,InvestmentGuideLine,InvestorComplaintFormat,AffectedSmallInvestorNotice,AffectedSmallInvestorCategory,AffectedSmallInvestorDetails,CautionNotice,IpoLotteryResult

# Register your models here.
admin.site.register(TrainingNotice)
admin.site.register(InvestorEduProgram)
admin.site.register(InvestmentGuideLine)
admin.site.register(InvestorComplaintFormat)
admin.site.register(AffectedSmallInvestorNotice)
admin.site.register(AffectedSmallInvestorCategory)
admin.site.register(AffectedSmallInvestorDetails)
admin.site.register(CautionNotice)
admin.site.register(IpoLotteryResult)