from bdb import effective
from locale import currency
from urllib.request import Request
from django.shortcuts import render
# import wallet
from wallet .models import Wallet
from django import redirect
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

def customer_profile(request,id):
    customer = Customer.objects.get(id=id)
    return render(request,"wallet/customer_profile.html",{"customer":customer})

def edit_customer(request,id):
    customer = Customer.objects.get(id=id)
    request.method == "POST"   
    form = CustomerRegistrationForm(request.POST, instance= Customer) 

    if form.is_valid():
        form.save()
        return redirect("Customer_profile,id=customer.id")

    else:
        form=CustomerRegistrationForm(instance=customer)
        return render(request,"wallet/edit_customer.html",{form:form})



# def customer_profile(request,id):
#     customer = models.Customer.objects.get(id = id)
#     return render(request,"wallet/customer_profile.html",{"customer":customer})

# def edit_customer(request,id):
#     customer = models.Customer.objects.get(id=id)
#     if request.method == "POST":
#         form = forms.CustomerRegistrationForm(request.POST,instance=customer)
#     if form.is_valid():
#             form.save()
#             return redirect("customer_profile",id=customer.id)
#     else:
#         form =forms.CustomerRegistrationForm(instance=customer)
#         return render(request,"wallet/edit_customer.html",{"form":form})


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

def wallet_profile(request,id):
    wallet = Wallet.objects.get(id = id)
    return render(request,"wallet/wallet_profile.html",{"wallet":wallet})

def edit_wallet(request,id):
    wallet = Wallet.objects.get(id=id)
    if request.method == "POST":
        form = WalletRegistrationForm(request.POST,instance=wallet)
    if form.is_valid():
            form.save()
            return redirect("wallet_profile",id=wallet.id)
    else:
        form = WalletRegistrationForm(instance=wallet)
        return render(request,"wallet/edit_customer.html",{"form":form})


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

def list_accounts(request):
    accounts = Account.objects.all()
    return accounts(request, "wallet/account_list.html",
    {"accounts": accounts}) 

def account_profile(request,id):
    account = Account.objects.get(id = id)
    return render(request,"wallet/account_profile.html",{"account":account})

def edit_account(request,id):
    account = Account.objects.get(id=id)
    if request.method == "POST":
        form = AccountRegistrationForm(request.POST,instance=account)
    if form.is_valid():
            form.save()
            return redirect("account_profile",id=account.id)
    else:
        form = AccountRegistrationForm(instance=account)
        return render(request,"wallet/edit_customer.html",{"form":form})
         

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

def transaction_profile(request,id):
    transaction = Transaction.objects.get(id = id)
    return render(request,"wallet/transaction_profile.html",{"transaction":transaction})

def edit_transaction(request,id):
    transaction = Transaction.objects.get(id=id)
    if request.method == "POST":
        form = TransactionRegistrationForm(request.POST,instance=transaction)
    if form.is_valid():
            form.save()
            return redirect("transaction_profile",id=transaction.id)
    else:
        form = TransactionRegistrationForm(instance=transaction)
        return render(request,"wallet/edit_transaction.html",{"form":form})
        

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

def card_profile(request,id):
    card = Card.objects.get(id = id)
    return render(request,"wallet/card_profile.html",{"card":card})

def edit_card(request,id):
    card = Card.objects.get(id=id)
    if request.method == "POST":
        form = CardRegistrationForm(request.POST,instance=card)
    if form.is_valid():
            form.save()
            return redirect("card_profile",id=card.id)
    else:
        form = CardRegistrationForm(instance=card)
        return render(request,"wallet/edit_card.html",{"form":form})
         

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
        return render(request,"wallet/register_third_party.html",
        {"form":form})

def list_third_partys(request):
    third_partys = Third_party.objects.all()
    return third_partys(request, "wallet/third_party_list.html",
    {"third_partys": third_partys})  

def third_party_profile(request,id):
    third_party = Third_party.objects.get(id = id)
    return render(request,"wallet/third_party_profile.html",{"third_party":third_party})

def edit_third_party(request,id):
    third_party = Third_party.objects.get(id=id)
    if request.method == "POST":
        form = Third_partyRegistrationForm(request.POST,instance=third_party)
    if form.is_valid():
            form.save()
            return redirect("customer_profile",id=third_party.id)
    else:
        form = Third_partyRegistrationForm(instance=third_party)
        return render(request,"wallet/edit_third_party.html",{"form":form})
          
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
        return render(request,"wallet/register_notifications.html",
        {"form":form})

def list_notifications(request):
    notifications = Notifications.objects.all()
    return notifications(request, "wallet/notifications_list.html",
    {"notifications": notifications}) 

def notification_profile(request,id):
    notification = Notifications.objects.get(id = id)
    return render(request,"wallet/notification_profile.html",{"notification":notification})

def edit_notification(request,id):
    notification = Notifications.objects.get(id=id)
    if request.method == "POST":
        form = NotificationsRegistrationForm(request.POST,instance=notification)
    if form.is_valid():
            form.save()
            return redirect("customer_profile",id=notification.id)
    else:
        form = NotificationsRegistrationForm(instance=notification)
        return render(request,"wallet/edit_notification.html",{"form":form})
   
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

def receipt_profile(request,id):
    receipt = Reciept.objects.get(id = id)
    return render(request,"wallet/receipt_profile.html",{"receipt":receipt})

def edit_receipt(request,id):
    receipt = Reciept.objects.get(id=id)
    if request.method == "POST":
        form = ReceiptRegistrationForm(request.POST,instance=receipt)
    if form.is_valid():
            form.save()
            return redirect("receipt_profile",id=receipt.id)
    else:
        form = ReceiptRegistrationForm(instance=receipt)
        return render(request,"wallet/edit_receipt.html",{"form":form})
   

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

def loan_profile(request,id):
    loan = Loan.objects.get(id = id)
    return render(request,"wallet/loan_profile.html",{"loan":loan})

def edit_loan(request,id):
    loan = Loan.objects.get(id=id)
    if request.method == "POST":
        form = LoanRegistrationForm(request.POST,instance=loan)
    if form.is_valid():
            form.save()
            return redirect("loan_profile",id=loan.id)
    else:
        form = LoanRegistrationForm(instance=loan)
        return render(request,"wallet/edit_loan.html",{"form":form})
  
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

def reward_profile(request,id):
    reward = Reward.objects.get(id = id)
    return render(request,"wallet/customer_profile.html",{"reward":reward})

def edit_reward(request,id):
    reward = Reward.objects.get(id=id)
    if request.method == "POST":
        form = RewardRegistrationForm(request.POST,instance=reward)
    if form.is_valid():
            form.save()
            return redirect("reward_profile",id=reward.id)
    else:
        form = RewardRegistrationForm(instance=reward)
        return render(request,"wallet/edit_reward.html",{"form":form})
  
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

def currency_profile(request,id):
    currency = Currency.objects.get(id = id)
    return render(request,"wallet/currency_profile.html",{"currency":currency})

def edit_currency(request,id):
    currency = Currency.objects.get(id=id)
    if request.method == "POST":
        form = CurrencyRegistrationForm(request.POST,instance=currency)
    if form.is_valid():
            form.save()
            return redirect("currency_profile",id=currency.id)
    else:
        form = CurrencyRegistrationForm(instance=currency)
        return render(request,"wallet/edit_currency.html",{"form":form})
    
    # return render(request,"wallet/register_currency.html",
    # {"form":form})   

