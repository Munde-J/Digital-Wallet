import email
from locale import currency
from pyexpat import model
from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name  = models.CharField(max_length=20)
    address = models.TextField()
    email = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    age = models.PositiveSmallIntegerField()

class Wallet(models.Model):
    balance = models.IntegerField()
    customer = models.ForeignKey('customer',on_delete=models.CASCADE,related_name='Wallet_customer')
    amount = models.IntegerField()
    time = models.DateTimeField()
    currency = models.ForeignKey('currency',on_delete=models.CASCADE,related_name='Wallet_currency')
    status = models.CharField(max_length=20)

class Account(models.Model):
    account_number = models.IntegerField()
    account_type = models.CharField(max_length=20)
    account_balance = models.IntegerField()
    account_name = models.CharField(max_length=20)
    wallet = models.ForeignKey('wallet',on_delete=models.CASCADE,related_name='Account_wallet')

class Transaction(models.Model):
    transaction_ref = models.CharField(max_length=20)
    wallet = models.ForeignKey('wallet',on_delete=models.CASCADE,related_name='Transaction_wallet')
    transaction_amount = models.IntegerField()
    transaction_name = models.CharField(max_length=20)
    transaction_type = models.CharField(max_length=20)
    transaction_charge = models.IntegerField()
    date_and_time = models.DateTimeField()
    destination_account = models.IntegerField()
    receipt = models.CharField(max_length=20)
class Card(models.Model):
    card_number = models.IntegerField()
    card_name = models.CharField(max_length=20)
    date_issued = models.DateTimeField()
    card_type = models.CharField(max_length=20)
    expiry_date = models.IntegerField()
    security_code = models.IntegerField()
    wallet = models.ForeignKey('wallet',on_delete=models.CASCADE,related_name='Card_wallet')
    account = models.ForeignKey('account',on_delete=models.CASCADE,related_name='Card_account')
    issuer = models.CharField(max_length=20)

class Third_party(models.Model):
    name = models.CharField(max_length=20)
    currency = models.ForeignKey('currency',on_delete=models.CASCADE,related_name='Third_party_currency')
    account = models.ForeignKey('account',on_delete=models.CASCADE,related_name='Third_party_account')
    type = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    amount = models.IntegerField()

class Notifications(models.Model):
    transaction_description = models.CharField(max_length=20)
    transaction_id = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    recipient = models.OneToOneField(Customer,on_delete=models.CASCADE,related_name='Notifications_recipient')
    status = models.CharField(max_length=20)
    date_and_time = models.DateTimeField()

class Reciept(models.Model):
    reciept_type = models.CharField(max_length=20)
    date = models.DateField()
    bill_number = models.CharField(max_length=20)
    balance = models.IntegerField()
    amount = models.IntegerField()
    transaction = models.ForeignKey('transaction',on_delete=models.CASCADE,related_name='Reciept_transaction')
    receipt_file = models.FileField()

class Loan(models.Model):
    loan_number = models.IntegerField()
    date_and_time = models.DateTimeField()
    amount = models.IntegerField()
    loan_status = models.CharField(max_length=20)
    wallet = models.ForeignKey('wallet',on_delete=models.CASCADE,related_name='Loan_wallet')
    interest_rate = models.IntegerField()
    loan_term = models.CharField
    payment_due_date = models.DateTimeField()
    loan_balance = models.IntegerField()
    guarantor = models.CharField(max_length=20)

class Reward(models.Model):
    transaction = models.CharField(max_length=20)
    customer_id = models.IntegerField()
    points = models.IntegerField()
    gender = models.CharField(max_length=20)
    third_party = models.ForeignKey('third_party',on_delete=models.CASCADE,related_name='Reward_third_party')
    date_time = models.DateTimeField()

class Currency(models.Model):
    origin = models.CharField(max_length=20) 
    symbol = models.CharField(max_length=20)
    amount = models.IntegerField()

    


    



    





