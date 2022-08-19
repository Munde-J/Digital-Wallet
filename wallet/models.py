
from django.utils import timezone
from django.db import models

# Create your models here.
class Customer(models.Model):
    profile_picture = models.ImageField(upload_to='profile_picture', null=True,)
    first_name = models.CharField(max_length=20,null=True)
    last_name  = models.CharField(max_length=20,null=True)
    address = models.TextField()
    email = models.CharField(max_length=15,null=True)
    gender = models.CharField(max_length=10,null=True)
    age = models.PositiveSmallIntegerField()

class Wallet(models.Model):
    balance = models.IntegerField()
    customer = models.ForeignKey('Customer',on_delete=models.CASCADE,related_name='Wallet_customer')
    amount = models.IntegerField()
    time = models.DateTimeField(default=timezone.now)
    currency = models.ForeignKey('Currency',on_delete=models.CASCADE,related_name='Wallet_currency')

class Account(models.Model):
    account_number = models.IntegerField()
    account_type = models.CharField(max_length=20,null=True)
    account_balance = models.IntegerField()
    account_name = models.CharField(max_length=20,null=True)
    wallet = models.ForeignKey('Wallet',on_delete=models.CASCADE,related_name='Account_wallet')

class Transaction(models.Model):
    transaction_ref = models.CharField(max_length=20,null=True)
    wallet = models.ForeignKey('Wallet',on_delete=models.CASCADE,related_name='Transaction_wallet')
    transaction_amount = models.IntegerField()
    transaction_type = models.CharField(max_length=20,null=True)
    transaction_charge = models.IntegerField()
    date_and_time = models.DateTimeField(default=timezone.now)
    destination_account = models.IntegerField()
    receipt = models.CharField(max_length=20,null=True)
    origin = models.CharField(max_length=20,null=True)

    
class Card(models.Model):
    card_number = models.IntegerField()
    card_name = models.CharField(max_length=20,null=True)
    date_issued = models.DateTimeField(default=timezone.now)
    card_type = models.CharField(max_length=20,null=True)
    expiry_date = models.DateTimeField(default=timezone.now)
    security_code = models.IntegerField()
    wallet = models.ForeignKey('Wallet',on_delete=models.CASCADE,related_name='Card_wallet')
    account = models.ForeignKey('Account',on_delete=models.CASCADE,related_name='Card_account')
    issuer = models.CharField(max_length=20,null=True)

class Third_party(models.Model):
    name = models.CharField(max_length=20,null=True)
    currency = models.ForeignKey('Currency',on_delete=models.CASCADE,related_name='Third_party_currency')
    account = models.ForeignKey('Account',on_delete=models.CASCADE,related_name='Third_party_account')
    location = models.CharField(max_length=20,null=True)
    amount = models.IntegerField()

class Notifications(models.Model):
    transaction_description = models.CharField(max_length=20,null=True)
    # choice_type
    transaction_id = models.CharField(max_length=20,null=True)
    title = models.CharField(max_length=20,null=True)
    recipient = models.OneToOneField(Customer,on_delete=models.CASCADE,related_name='Notifications_recipient')
    status = models.CharField(max_length=20,null=True)
    date_and_time = models.DateTimeField(default=timezone.now)

class Reciept(models.Model):
    CHOICE = (
        ('withdraw','withdraw'),
        ('deposit','deposit'),
    )
    reciept_type = models.CharField(max_length=20,null=True,choices=CHOICE)
    date = models.DateField()
    bill_number = models.CharField(max_length=20,null=True)
    balance = models.IntegerField()
    amount = models.IntegerField()
    transaction = models.ForeignKey('Transaction',on_delete=models.CASCADE,related_name='Reciept_transaction')
    receipt_file = models.FileField()

class Loan(models.Model):
    loan_number = models.IntegerField()
    date_and_time = models.DateTimeField()
    amount = models.IntegerField()
    loan_status = models.CharField(max_length=20,null=True)
    wallet = models.ForeignKey('Wallet',on_delete=models.CASCADE,related_name='Loan_wallet')
    interest_rate = models.IntegerField()
    loan_term = models.CharField(max_length=20,null=True)
    payment_due_date = models.DateTimeField(default=timezone.now)
    loan_balance = models.IntegerField()
    guarantor = models.CharField(max_length=20,null=True)

class Reward(models.Model):
    transaction = models.CharField(max_length=20,null=True)
    customer_id = models.IntegerField()
    points = models.IntegerField()
    gender = models.CharField(max_length=20,null=True)
    third_party = models.ForeignKey('Third_party',on_delete=models.CASCADE,related_name='Reward_third_party')
    date_time = models.DateTimeField(default=timezone.now)

class Currency(models.Model):
    origin = models.CharField(max_length=20,null=True) 
    symbol = models.CharField(max_length=20,null=True)
    amount = models.IntegerField()

    


    



    





