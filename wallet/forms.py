from django import forms
from .models import Currency, Customer, Notifications, Third_party
from django.forms import ModelForm
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


class CustomerRegistrationForm(ModelForm):
    # meta class provides data for the class you're inheriting from'
  class Meta:
        model=Customer
        fields=("first_name","last_name","address","email","gender","age")
        widgets={
          "first_name":forms.TextInput(attrs={'class':'form-control'}),
          "last_name":forms.TextInput(attrs={'class':'form-control'}),
          "address":forms.TextInput(attrs={'class':'form-control'}),
          "email":forms.TextInput(attrs={'class':'form-control'}),     
          "gender":forms.TextInput(attrs={'class':'form-control'}),    
          "age":forms.TextInput(attrs={'class':'form-control'}),
        }

class WalletRegistrationForm(ModelForm):
  class Meta:
        model=Wallet
        fields=("balance","customer","amount","time","currency") 
        widgets={
          "balance":forms.TextInput(attrs={'class':'form-control'}),
          "customer":forms.TextInput(attrs={'class':'form-control'}),     
          "amount":forms.TextInput(attrs={'class':'form-control'}),    
          "time":forms.TextInput(attrs={'class':'form-control'}),
          "currency":forms.TextInput(attrs={'class':'form-control'}),    
        }

class AccountRegistrationForm(ModelForm):
  class Meta:
        model=Account
        fields=("account_name","account_number","account_type","account_balance","wallet")
        widgets={
          "account_name":forms.TextInput(attrs={'class':'form-control'}),
          "account_number":forms.TextInput(attrs={'class':'form-control'}),     
          "account_type":forms.TextInput(attrs={'class':'form-control'}),    
          "account_balance":forms.TextInput(attrs={'class':'form-control'}),
          "wallet":forms.TextInput(attrs={'class':'form-control'}),    
        }

class TransactionRegistrationForm(ModelForm):
  class Meta:
        model=Transaction
        fields=("transaction_ref","transaction_amount","transaction_type","transaction_charge","date_and_time","destination_account","receipt","origin")
        widgets={
          "transaction_ref":forms.TextInput(attrs={'class':'form-control'}),
          "transaction_amount":forms.TextInput(attrs={'class':'form-control'}),
          "transaction_type":forms.TextInput(attrs={'class':'form-control'}),
          "transaction_charge":forms.TextInput(attrs={'class':'form-control'}),     
          "date_and_time":forms.TextInput(attrs={'class':'form-control'}),    
          "destination_account":forms.TextInput(attrs={'class':'form-control'}),
          "receipt":forms.TextInput(attrs={'class':'form-control'}),
          "origin":forms.TextInput(attrs={'class':'form-control'}),
        }

class CardRegistrationForm(ModelForm):
  class Meta:
        model=Card
        fields=("card_name","card_number","card_type","date_issued","expiry_date","security_code","wallet","account","issuer")
        widgets={
          "card_name":forms.TextInput(attrs={'class':'form-control'}),
          "card_number":forms.TextInput(attrs={'class':'form-control'}),
          "card_type":forms.TextInput(attrs={'class':'form-control'}),
          "date_issued":forms.TextInput(attrs={'class':'form-control'}),     
          "expiry_date":forms.TextInput(attrs={'class':'form-control'}),    
          "security_code":forms.TextInput(attrs={'class':'form-control'}),
          "wallet":forms.TextInput(attrs={'class':'form-control'}),
          "account":forms.TextInput(attrs={'class':'form-control'}),
          "issuer":forms.TextInput(attrs={'class':'form-control'}),
        }  

class Third_partyRegistrationForm(ModelForm):
  class Meta:
        model=Third_party
        fields=("name","account","currency","location","amount")
        widgets ={
        "name":forms.TextInput(attrs={'class':'form-control'}),    
        "account":forms.TextInput(attrs={'class':'form-control'}),
        "currency":forms.TextInput(attrs={'class':'form-control'}),
        "location":forms.TextInput(attrs={'class':'form-control'}),
        "amount":forms.TextInput(attrs={'class':'form-control'}),
        }

class NotificationsRegistrationForm(ModelForm):
  class Meta:
        model=Notifications
        fields=("transaction_id", "transaction_description", "title","recipient","status","date_and_time")
        widgets = {
        "transaction_id":forms.TextInput(attrs={'class':'form-control'}),
          "transaction_description":forms.TextInput(attrs={'class':'form-control'}),
          "title":forms.TextInput(attrs={'class':'form-control'}),
          "recipient":forms.TextInput(attrs={'class':'form-control'}),     
          "status":forms.TextInput(attrs={'class':'form-control'}),    
          "date_and_time":forms.TextInput(attrs={'class':'form-control'}),    
          }

class ReceiptRegistrationForm(ModelForm):
  class Meta:
        model=Reciept
        fields=("CHOICE", "receipt_type", "date","bill_number","balance","amount","transaction","receipt_file")
        widgets ={
          "CHOICE":forms.TextInput(attrs={'class':'form-control'}),
          "receipt_type":forms.TextInput(attrs={'class':'form-control'}),
          "date":forms.TextInput(attrs={'class':'form-control'}),     
          "bill_number":forms.TextInput(attrs={'class':'form-control'}),    
          "balance":forms.TextInput(attrs={'class':'form-control'}),
          "amount":forms.TextInput(attrs={'class':'form-control'}),
          "transaction":forms.TextInput(attrs={'class':'form-control'}),
          "receipt_file":forms.TextInput(attrs={'class':'form-control'}),
        }  

class LoanRegistrationForm(ModelForm):
  class Meta:
        model=Loan
        fields=("loan_number","date_and_time","amount","loan_status","wallet","interest_rate","payment_due_date","loan_term","loan_balance","guarantor")
        widgets={
          "loan_number":forms.TextInput(attrs={'class':'form-control'}),
          "date_and_time":forms.TextInput(attrs={'class':'form-control'}),
          "amount":forms.TextInput(attrs={'class':'form-control'}),
          "loan_status":forms.TextInput(attrs={'class':'form-control'}),     
          "wallet":forms.TextInput(attrs={'class':'form-control'}),    
          "interest_rate":forms.TextInput(attrs={'class':'form-control'}),
          "payment_due_date":forms.TextInput(attrs={'class':'form-control'}),
          "loan_term":forms.TextInput(attrs={'class':'form-control'}),
          "loan_balance":forms.TextInput(attrs={'class':'form-control'}),
          "guarantor":forms.TextInput(attrs={'class':'form-control'}),

        }  

class RewardRegistrationForm(ModelForm):
  class Meta:
        model=Reward
        fields=("transaction","customer_id","points","gender","third_party","date_time")
        widgets = {
          "transaction":forms.TextInput(attrs={'class':'form-control'}),    
          "customer_id":forms.TextInput(attrs={'class':'form-control'}),
          "points":forms.TextInput(attrs={'class':'form-control'}),
          "gender":forms.TextInput(attrs={'class':'form-control'}),
          "third_party":forms.TextInput(attattrs={'class':'form-control'}),
          "date_time":forms.TextInput(attrs={'class':'form-control'}),
        }

class CurrencyRegistrationForm(ModelForm):
  class Meta:
        model=Currency
        fields=("origin","symbol","amount")
        widgets= {
          "origin":forms.TextInput(attrs={'class':'form-control'}),
          "symbol":forms.TextInput(attattrs={'class':'form-control'}),
          "amount":forms.TextInput(attrs={'class':'form-control'}),
        }