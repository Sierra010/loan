from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="homePage"),
    path('loan/', views.LoanPage, name="loanPage"),
    path('payloan/', views.paidLoan, name="payLoan"),
    path('loanhistory/', views.loanHistory, name="loanHisotry")
]
