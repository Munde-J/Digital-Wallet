from django.urls import path
from .views import customer_profile, edit_customer, register_account, register_currency, register_customer, register_notifications, register_receipt, register_reward, register_transaction
from .views import register_wallet
from .views import register_card
from .views import register_third_party
from .views import register_notifications
from .views import register_receipt
from .views import register_loan
from .views import register_reward
from . import views

from .views import list_accounts
from .views import list_cards
from .views import list_currencys
from .views import list_customers
from .views import list_loan
from .views import list_notifications
from .views import list_receipts
from .views import list_rewards
from .views import list_third_partys
from .views import list_wallets
from .views import list_transactions


urlpatterns = [
    path("customer/", register_customer, name = "registration"),
    path("customers/", views.list_customers, name="customers_list"),
 
    path("wallet/",register_wallet, name="registration"),
    path("wallets/", views.list_wallets, name="wallets_list"),

    path("account/",register_account, name="registration"),
    path("accounts/", views.list_accounts, name="accounts_list"),

    path("transaction/",register_transaction, name="registration"),
    path("transactions/", views.list_customers, name="transactions_list"),

    path("card/",register_card, name="registration"),
    path("card/", views.list_cards, name="card_list"),

    path("third_party/",register_third_party, name="registration"),
    path("third_party/", views.list_third_partys, name="third_party_list"),

    path("notifications/",register_notifications, name="registration"),
    path("notifications/", views.list_notifications, name="notifications_list"),

    path("receipt/",register_receipt, name="registration"),
    path("receipts/", views.list_receipts, name="receipts_list"),

    path("loan/",register_loan, name="registration"),
    path("loans/", views.list_loan, name="loans_list"),

    path("reward/",register_reward, name="registration"),
    path("rewards/", views.list_rewards, name="reward_list"),

    path("currency/",register_currency, name="registration"),
    path("currency/", views.list_currencys, name="currency_list"),

    path("customers/edit/<int:id/",edit_customer, name="edit_customer"),

    # path("customers/<int:id>",customer_profile,name="customer_profile") 








]

