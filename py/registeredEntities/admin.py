from django.contrib import admin
from . models import StockExchanges,CentralDepository,MerchantBankersList,CreditRatingAgenciesList,AssetManagementCompaniesList,CustodiansList,TrusteesList,FundManagersList

# Register your models here.

admin.site.register(StockExchanges)
admin.site.register(CentralDepository)
admin.site.register(MerchantBankersList)
admin.site.register(CreditRatingAgenciesList)
admin.site.register(AssetManagementCompaniesList)
admin.site.register(CustodiansList)
admin.site.register(TrusteesList)
admin.site.register(FundManagersList)