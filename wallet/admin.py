from django.contrib import admin

# Register your models here.
from .models import Customer
from .models import Wallet
from .models import Account
from .models import Transaction
from .models import Card
from .models import Third_party
from .models import Notifications
from .models import Reciept
from .models import Loan
from .models import Reward
from .models import Currency



class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','age','email',)
    search_fields = ('first_name','last_name',)
admin.site.register(Customer,CustomerAdmin)

class AccountAdmin(admin.ModelAdmin):
    list_display = ('account_number','account_type','account_balance',)
    search_fields = ('account_number','account_type','account_balance',)
admin.site.register(Account,AccountAdmin)  

class CardAdmin(admin.ModelAdmin):
    list_display = ('card_name','card_number','card_type',)
    search_fields = ('card_name','card_number','card_type',)
admin.site.register(Card,CardAdmin)

class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('origin','symbol','amount',)
    search_fields = ('origin','symbol','amount',)
admin.site.register(Currency,CurrencyAdmin)

    

class LoanAdmin(admin.ModelAdmin):
    list_display = ('loan_number','amount','loan_status',)
    search_fields = ('loan_number','amount','loan_status',)
admin.site.register(Loan,LoanAdmin)


class NotificationAdmin(admin.ModelAdmin):
    list_display = ('transaction_id','recipient','status',)
    search_fields = ('transaction_id','recipient','status',)
admin.site.register(Notifications,NotificationAdmin)

class RecieptAdmin(admin.ModelAdmin):
    list_display = ('date','bill_number',)
    search_fields = ('reciept_type','date','bill_number',)
admin.site.register(Reciept,RecieptAdmin)

class RewardAdmin(admin.ModelAdmin):
    list_display = ('customer_id','transaction','points',)
    search_fields = ('customer_id','transaction','points',)
admin.site.register(Reward,RewardAdmin)    


class Third_partyAdmin(admin.ModelAdmin):
    list_display = ('currency','amount','account',)
    search_fields = ('currency','amount','account',)
admin.site.register(Third_party,Third_partyAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_ref','wallet','transaction_amount',)
    search_fields = ('transaction_ref','wallet','transaction_amount',)
admin.site.register(Transaction,TransactionAdmin)

class WalletAdmin(admin.ModelAdmin):
    list_display = ('balance','customer','amount',)
    search_fields = ('balance','customer','amount',)
admin.site.register(Wallet,WalletAdmin)


    
    








