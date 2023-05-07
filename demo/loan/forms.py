from django.forms import ModelForm
from django import forms

from .models import *


class LoanForm(ModelForm):
    class Meta:
        model = Loan
        fields = [
            'customerid',
            'Loanamount',
            'Intrest',
            'PayPerInstallment',
            'Installment_time',
            'Guaranter_card_id',
            'status'
        ]


class PayLoanForm(ModelForm):
    class Meta:
        model = LoanRecord
        fields = '__all__'
