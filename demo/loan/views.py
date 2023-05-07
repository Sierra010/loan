from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect

from .forms import LoanForm, PayLoanForm
from .models import *
# Create your views here.


def home(request):
    return render(request, 'loan/homePage.html')


def LoanPage(request):

    form = LoanForm()

    #-- Code Generator
    alphanumeric = ['']

    if request.method == "POST":
        form = LoanForm(request.POST)
        guaranter_id_input = request.POST.get('Guaranter_card_id')

        # Check if guaranter is in database and can be guaranter
        try:
            guaranter = Customer.objects.get(card_num=guaranter_id_input)
        except Customer.DoesNotExist:
            raise Http404

        if guaranter.guaranter_time > 0:
            print("[**] Allow to be guaranter")
            guaranter.guaranter_time -= 1
            form.save()
            guaranter.save()
        else:
            print("[!] This person can't be a guaranter")

    context = {"form": LoanForm}
    return render(request, 'loan/LoanPage.html', context)


def paidLoan(request):

    form = PayLoanForm()

    if request.method == "POST":

        loanpk = request.POST.get('Loanid')
        installment_inp = request.POST.get('Installment_time')
        try:
            loan_data = Loan.objects.get(pk=loanpk)
        except Loan.DoesNotExist:
            return Http404

        loan_data.Installment_time -= int(installment_inp)
        loan_data.save()

    context = {'form': form}
    return render(request, 'loan/LoanPage.html', context)


def loanHistory(request):

    context = {}
    return render(request, 'loan/loanhistory.html', context)
