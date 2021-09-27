from django.contrib import admin
from . models import LawList,CategoryList,SecuritiesLaw,securitiesLawsBook,CommentsDratfRules

# Register your models here.

admin.site.register(LawList)
admin.site.register(CategoryList)
admin.site.register(SecuritiesLaw)
admin.site.register(securitiesLawsBook)
admin.site.register(CommentsDratfRules)