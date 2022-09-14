from locale import currency
from django.shortcuts import render
from wallet .models import Wallet
from .forms import CustomerRegistrationForm
from .models import Account, Card, Currency, Customer, Loan, Notifications, Reciept, Reward, Third_party, Transaction
# from . import forms
from .forms import WalletRegistrationForm
from .forms import AccountRegistrationForm
from .forms import TransactionRegistrationForm
from .forms import CardRegistrationForm
from .forms import Third_partyRegistrationForm
from .forms import NotificationsRegistrationForm
from .forms import ReceiptRegistrationForm
from .forms import LoanRegistrationForm
from .forms import RewardRegistrationForm
from .forms import CurrencyRegistrationForm

# Create your views here.
def register_customer(request):
    form = CustomerRegistrationForm()
    if request.method == "POST":
        form = CustomerRegistrationForm(request.POST)
    if form.is_valid():
        form.save()
    else:
        form = CustomerRegistrationForm()
        return render(request,"wallet/register_customer.html",
        {"form":form})

def list_customers(request):
    customers = Customer.objects.all()
    return customers(request, "wallet/customers_list.html",
    {"customers": customers})
    # return render(request,"wallet/register_customer.html",
    # {"form":form})

def register_wallet(request):
    form = WalletRegistrationForm()
    if request.method == "POST":
        form = WalletRegistrationForm(request.POST)
    if form.is_valid():
        form.save()
    else:
        form = WalletRegistrationForm()
        return render(request,"wallet/register_wallet.html",
        {"form":form})

def list_wallets(request):
    wallets = Wallet.objects.all()
    return wallets(request, "wallet/wallets_list.html",
    {"wallets": wallets})       
    # return render(request,"wallet/register_wallet.html",
    # {"form":form})

def register_account(request):
    form = AccountRegistrationForm()
    if request.method == "POST":
        form = AccountRegistrationForm(request.POST)
    if form.is_valid():
        form.save()
    else:
        form = AccountRegistrationForm()
        return render(request,"wallet/register_account.html",
        {"form":form})

def list_wallets(request):
    accounts = Account.objects.all()
    return accounts(request, "wallet/account_list.html",
    {"accounts": accounts})          

    # return render(request,"wallet/register_account.html",
    # {"form":form})

def register_transaction(request):
    form = TransactionRegistrationForm()
    if request.method == "POST":
        form = TransactionRegistrationForm(request.POST)
    if form.is_valid():
        form.save()
    else:
        form = TransactionRegistrationForm()
        return render(request,"wallet/register_transaction.html",
        {"form":form})

def list_transactions(request):
    transactions = Transaction.objects.all()
    return transactions(request, "wallet/transaction_list.html",
    {"transactions": transactions})          

    # return render(request,"wallet/register_transaction.html",
    # {"form":form})  

def register_card(request):
    form = CardRegistrationForm()
    if request.method == "POST":
        form = CardRegistrationForm(request.POST)
    if form.is_valid():
        form.save()
    else:
        form = CardRegistrationForm()
        return render(request,"wallet/register_card.html",
        {"form":form})

def list_cards(request):
    cards = Card.objects.all()
    return cards(request, "wallet/card_list.html",
    {"cards": cards})          

    # return render(request,"wallet/register_card.html",
    # {"form":form}) 

def register_third_party(request):
    form = Third_partyRegistrationForm()
    if request.method == "POST":
        form = Third_partyRegistrationForm(request.POST)
    if form.is_valid():
        form.save()
    else:
        form = Third_partyRegistrationForm()
        return render(request,"wallet/register_card.html",
        {"form":form})

def list_third_partys(request):
    third_partys = Third_party.objects.all()
    return third_partys(request, "wallet/third_party_list.html",
    {"third_partys": third_partys})            
    # return render(request,"wallet/register_third_party.html",
    # {"form":form})

def register_notifications(request):
    form = NotificationsRegistrationForm()
    if request.method == "POST":
        form = NotificationsRegistrationForm(request.POST)
    if form.is_valid():
        form.save()
    else:
        form = NotificationsRegistrationForm()
        return render(request,"wallet/register_notification.html",
        {"form":form})

def list_notifications(request):
    notifications = Notifications.objects.all()
    return notifications(request, "wallet/notification_list.html",
    {"notifications": notifications})    
    # return render(request,"wallet/register_notifications.html",
    # {"form":form}) 

def register_receipt(request):
    form = ReceiptRegistrationForm()
    if request.method == "POST":
        form = ReceiptRegistrationForm(request.POST)
    if form.is_valid():
        form.save()
    else:
        form = ReceiptRegistrationForm()
        return render(request,"wallet/register_receipt.html",
        {"form":form})

def list_receipts(request):
    receipts = Reciept.objects.all()
    return receipts(request, "wallet/receipt_list.html",
    {"receipts": receipts})    

def register_loan(request):
    form = LoanRegistrationForm()
    if request.method == "POST":
        form = LoanRegistrationForm(request.POST)
    if form.is_valid():
        form.save()
    else:
        form = LoanRegistrationForm()
        return render(request,"wallet/register_loan.html",
        {"form":form})

def list_loan(request):
    loans = Loan.objects.all()
    return loans(request, "wallet/loan_list.html",
    {"loans": loans})   
    # return render(request,"wallet/register_loan.html",
    # {"form":form}) 

def register_reward(request):
    form = RewardRegistrationForm()
    if request.method == "POST":
        form = RewardRegistrationForm(request.POST)
    if form.is_valid():
        form.save()
    else:
        form = RewardRegistrationForm()
        return render(request,"wallet/register_reward.html",
        {"form":form})

def list_rewards(request):
    rewards = Reward.objects.all()
    return rewards(request, "wallet/reward_list.html",
    {"rewards": rewards})   
    # return render(request,"wallet/register_reward.html",
    # {"form":form}) 

def register_currency(request):
    form = CurrencyRegistrationForm()
    if request.method == "POST":
        form = CurrencyRegistrationForm(request.POST)
    if form.is_valid():
        form.save()
    else:
        form = CurrencyRegistrationForm()
        return render(request,"wallet/register_currency.html",
        {"form":form})

def list_currencys(request):
    currency = Currency.objects.all()
    return currency(request, "wallet/currency_list.html",
    {"currency":currency})   
    # return render(request,"wallet/register_currency.html",
    # {"form":form})                           
