from django .urls import path
from wallet.models import Notifications
from .views import register_account
from .views import register_card
from . import views
from .views import register_currency
from .views import register_customer
from .views import register_loan
from .views import register_notifications
from .views import register_wallet
from .views import register_receipt
from .views import register_reward
from .views import register_third_party
from .views import edit_third_party
from .views import register_transaction
from .views import customer_profile
from .views import edit_customer
from .views import wallet_profile
from .views import edit_wallet
from .views import edit_currency
from .views import currency_profile
from .views import account_profile
from .views import edit_account
from .views import edit_reward
from .views import reward_profile
from .views import edit_transaction
from .views import transaction_profile
from .views import card_profile
from .views import edit_card
from .views import edit_notification
from .views import notification_profile
from .views import third_party_profile
from .views import loan_profile
from .views import edit_loan
from .views import receipt_profile
from .views import edit_receipt
# from django.urls import path
# from .views import account_profile, card_profile, currency_profile, customer_profile, edit_account, edit_card, edit_currency, edit_customer, edit_loan, edit_notification, edit_receipt, edit_reward, edit_third_party, edit_transaction, edit_wallet, loan_profile, notification_profile, receipt_profile, register_account, register_currency, register_customer, register_notifications, register_receipt, register_reward, register_transaction, reward_profile, third_party_profile, transaction_profile, wallet_profile
# from .views import register_wallet
# from .views import register_card
# from .views import register_third_party
# from .views import register_notifications
# from .views import register_receipt
# from .views import register_loan
# from .views import register_reward
# from . import views

# from .views import list_accounts
# from .views import list_cards
# from .views import list_currencys
# from .views import list_customers
# from .views import list_loan
# from .views import list_notifications
# from .views import list_receipts
# from .views import list_rewards
# from .views import list_third_partys
# from .views import list_wallets
# from .views import list_transactions


urlpatterns = [
    path("customer/", register_customer, name = "registration"),
    path("customers/", views.list_customers, name="customers_list"),
    path("customers/edit/<int:id/",edit_customer, name="edit_customer"),
    path("customer/<int:id>",customer_profile,name="customer_profile"), 
 
    path("wallet/",register_wallet, name="registration"),
    path("wallets/", views.list_wallets, name="wallets_list"),
    path("wallets/edit/<int:id/",edit_wallet, name="edit_wallet"),
    path("wallet/<int:id>",wallet_profile,name="wallet_profile"), 

    path("account/",register_account, name="registration"),
    path("accounts/", views.list_accounts, name="accounts_list"),
    path("accounts/edit/<int:id/",edit_account, name="edit_account"),
    path("account/<int:id>",account_profile,name="account_profile"), 

    path("transaction/",register_transaction, name="registration"),
    path("transactions/", views.list_customers, name="transactions_list"),
    path("transactions/edit/<int:id/",edit_transaction, name="edit_transaction"),
    path("transaction/<int:id>",transaction_profile,name="transaction_profile"), 

    path("card/",register_card, name="registration"),
    path("card/", views.list_cards, name="card_list"),
    path("cards/edit/<int:id/",edit_card, name="edit_card"),
    path("card/<int:id>",card_profile,name="card_profile"), 

    path("third_party/",register_third_party, name="registration"),
    path("third_party/", views.list_third_partys, name="third_party_list"),
    path("third_partys/edit/<int:id/",edit_third_party, name="edit_third_party"),
    path("third_party/<int:id>",third_party_profile,name="third_party_profile"), 

    path("notifications/",register_notifications, name="registration"),
    path("notifications/", views.list_notifications, name="notifications_list"),
    path("notifications/edit/<int:id/",edit_notification, name="edit_notification"),
    path("notification/<int:id>",notification_profile,name="notification_profile"), 

    path("receipt/",register_receipt, name="registration"),
    path("receipts/", views.list_receipts, name="receipts_list"),
    path("receipts/edit/<int:id/",edit_receipt, name="edit_receipt"),
    path("receipt/<int:id>",receipt_profile,name="receipt_profile"), 

    path("loan/",register_loan, name="registration"),
    path("loans/", views.list_loan, name="loans_list"),
    path("loans/edit/<int:id/",edit_loan, name="edit_loan"),
    path("loan/<int:id>",loan_profile,name="loan_profile"), 

    path("reward/",register_reward, name="registration"),
    path("rewards/", views.list_rewards, name="reward_list"),
    path("rewards/edit/<int:id/",edit_reward, name="edit_reward"),
    path("reward/<int:id>",reward_profile,name="reward_profile"), 

    path("currency/",register_currency, name="registration"),
    path("currency/", views.list_currencys, name="currency_list"),
    path("currencys/edit/<int:id/",edit_currency, name="edit_currency"),
    path("currency/<int:id>",currency_profile,name="currency_profile"), 
]

