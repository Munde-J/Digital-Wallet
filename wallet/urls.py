from django.urls import path
from .views import register_account, register_currency, register_customer, register_notifications, register_receipt, register_reward, register_transaction
from .views import register_wallet
from .views import register_card
from .views import register_third_party
from .views import register_notifications
from .views import register_receipt
from .views import register_loan
from .views import register_reward
from . import views
urlpatterns = [
    path("register/", register_customer, name = "registration"),
    path("customers/", views.list_customers, name="customers_list"),
 
    path("wallet/",register_wallet, name="registration"),
    path("account/",register_account, name="registration"),
    path("transaction/",register_transaction, name="registration"),
    path("card/",register_card, name="registration"),
    path("third_party/",register_third_party, name="registration"),
    path("notifications/",register_notifications, name="registration"),
    path("receipt/",register_receipt, name="registration"),
    path("loan/",register_loan, name="registration"),
    path("reward/",register_reward, name="registration"),
    path("currency/",register_currency, name="registration"),
    



    # path("customers/"views.list_customers)
    







]

