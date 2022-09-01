from django.urls import path
from .views import register_account, register_customer, register_transaction
from .views import register_wallet
from .views import register_card
urlpatterns = [
    path("register/", register_customer, name = "registration"),
    path("wallet/",register_wallet, name="registration"),
    path("wallet/",register_account, name="registration"),
    path("wallet/",register_transaction, name="registration"),
    path("wallet/",register_card, name="registration"),

]

