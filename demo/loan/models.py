from django.db import models

# Create your models here.


class Customer(models.Model):
    firstname = models.CharField(max_length=100, null=True)
    lastname = models.CharField(max_length=100, null=True)
    card_num = models.CharField(max_length=50, null=True)
    guaranter_time = models.PositiveSmallIntegerField(
        default=2, blank=True, null=True)

    def __str__(self):
        return self.firstname


class Loan(models.Model):

    STATUS = (
        ('Loaner', 'Loaner'),
        ('Paid', 'Paid')
    )

    customerid = models.ForeignKey(
        Customer, null=True, on_delete=models.SET_NULL)
    Loanamount = models.FloatField()
    Intrest = models.FloatField()
    PayPerInstallment = models.FloatField()
    Installment_time = models.PositiveSmallIntegerField()
    Guaranter_card_id = models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=50, null=True, choices=STATUS)
    TotalPaid = models.FloatField(null=True)

    def __str__(self):
        return str(self.customerid)


class LoanRecord(models.Model):
    Loanid = models.ForeignKey(Loan, null=True, on_delete=models.SET_NULL)
    Installment_time = models.PositiveSmallIntegerField(default=0)
    Amountpaid = models.FloatField()
    PaidDate = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.Loanid
