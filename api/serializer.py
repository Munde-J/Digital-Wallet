from rest_framework import serializers
from dataclasses import fields
from pyexpat import model

from wallet.models import (Account, Card, Customer, Loan, Notifications,
                           Reciept, Transaction, Wallet)


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'email', 'password', 'credit_card')
    
class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('balance', 'amount', 'status', 'currency')

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('account_number', 'account_type', 'account_balance', 'account_name')
    
class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('card_number', 'card_name', 'date_issued', 'card_type')

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('receipt', 'destination_account', 'transaction_type', 'transaction_number')

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ('loan_type', 'amount', 'loan_balance', 'guarantor')

class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reciept
        fields = ('receipt_type', 'bill_number', 'amount', 'customer')

class NotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = ('message', 'status', 'date_time', 'receipient')