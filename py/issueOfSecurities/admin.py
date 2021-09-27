from django.contrib import admin
from . models import IssueOfCapitalRules,PublicLimitedCompanyList,PrivateLimitedCompanyList,IpoFixedPriceRules,IpoFixedPriceCompanyList,IpoBookbuildingList,RpoList,RightIssuesOffer,DebtBondRules,DebtBondList,DebentureList,AssetBackedSecuritiesLaws,AssetBackedSecuritiesList,MutualFundRules,CloseFund,OpenFund,AltInvestmentFundRules,AltInvstmntFundData,ExchangeTradedFund,ReListing,PubIssueAppProcess

# Register your models here.

admin.site.register(IssueOfCapitalRules)
admin.site.register(PublicLimitedCompanyList)
admin.site.register(PrivateLimitedCompanyList)
admin.site.register(IpoFixedPriceRules)
admin.site.register(IpoFixedPriceCompanyList)
admin.site.register(IpoBookbuildingList)
admin.site.register(RpoList)
admin.site.register(RightIssuesOffer)
admin.site.register(DebtBondRules)
admin.site.register(DebtBondList)
admin.site.register(DebentureList)
admin.site.register(AssetBackedSecuritiesLaws)
admin.site.register(AssetBackedSecuritiesList)
admin.site.register(MutualFundRules)
admin.site.register(CloseFund)
admin.site.register(OpenFund)
admin.site.register(AltInvestmentFundRules)
admin.site.register(AltInvstmntFundData)
admin.site.register(ExchangeTradedFund)
admin.site.register(ReListing)
admin.site.register(PubIssueAppProcess)