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
        fields="__all__"

class WalletRegistrationForm(ModelForm):
  class Meta:
        model=Wallet
        fields="__all__" 

class AccountRegistrationForm(ModelForm):
  class Meta:
        model=Account
        fields="__all__"

class TransactionRegistrationForm(ModelForm):
  class Meta:
        model=Transaction
        fields="__all__"

class CardRegistrationForm(ModelForm):
  class Meta:
        model=Card
        fields="__all__"  

class Third_partyRegistrationForm(ModelForm):
  class Meta:
        model=Third_party
        fields="__all__" 

class NotificationsRegistrationForm(ModelForm):
  class Meta:
        model=Notifications
        fields="__all__" 

class ReceiptRegistrationForm(ModelForm):
  class Meta:
        model=Reciept
        fields="__all__"

class LoanRegistrationForm(ModelForm):
  class Meta:
        model=Loan
        fields="__all__" 

class RewardRegistrationForm(ModelForm):
  class Meta:
        model=Reward
        fields="__all__"

class CurrencyRegistrationForm(ModelForm):
  class Meta:
        model=Currency
        fields="__all__"                                                      
