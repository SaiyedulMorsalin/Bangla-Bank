from django.urls import path
from . import views

urlpatterns = [
    path("deposit/", views.DepositMoneyView.as_view(), name="deposit"),
    path("withdraw/", views.WithdrawMoneyView.as_view(), name="withdraw"),
    path(
        "transaction_report/",
        views.TransactionReportView.as_view(),
        name="transaction_report",
    ),
    path("loan_request/", views.LoanRequestView.as_view(), name="loan_request"),
    path("loan_list/", views.LoanListView.as_view(), name="loan_list"),
    path("pay_loan/<int:loan_id>/", views.PayLoanView.as_view(), name="pay_loan"),
    path("send_money/", views.SendMoney.as_view(), name="send_money"),
]
