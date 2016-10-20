from django.contrib import admin

from .models import Choice, Question, LifeInsurances,LifeInsuranceQuotes, Profiles,Providers, MortgageInsurances, MortgageInsuranceQuotes, FuneralInsurances, FuneralInsuranceQuotes, Companies


class LifeInsurancesInline(admin.TabularInline):
    model = LifeInsuranceQuotes
    extra = 0

class LifeInsurancesAdmin(admin.ModelAdmin):
    list_display = ('country_residence', 'cover_amount', 'residency_status')
    list_filter = ['created_at']
    search_fields = ['country_residence']
    inlines = [LifeInsurancesInline]


class FuneralInsurancesInline(admin.TabularInline):
    model = FuneralInsuranceQuotes
    extra = 0
 
class FuneralInsurancesAdmin(admin.ModelAdmin):
    list_display = ('user_email', 'cover_amount', 'residency_status')
    list_filter = ['created']
    search_fields = ['resident_country', 'user__email']
    inlines = [FuneralInsurancesInline]



class MortgageInsurancesInline(admin.TabularInline):
    model = MortgageInsuranceQuotes
    extra = 0

class MortgageInsurancesAdmin(admin.ModelAdmin):
    list_display = ('country_resident', 'mortgage_amount', 'resident_status')
    list_filter = ['mortgage_amount']
    search_fields = ['country_residence']
    inlines = [MortgageInsurancesInline]



class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # ...
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    inlines = [ChoiceInline]





admin.site.register(Question, QuestionAdmin)
admin.site.register(LifeInsurances,LifeInsurancesAdmin)
admin.site.register(MortgageInsurances,MortgageInsurancesAdmin)
admin.site.register(FuneralInsurances,FuneralInsurancesAdmin)
admin.site.register(Profiles)
admin.site.register(Providers)
admin.site.register(Companies)

