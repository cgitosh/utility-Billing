from http import client
import imp
from pyexpat import model
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.utils.translation import gettext_lazy as _
from accounts.models import BusinessAwareModel,User
from clients.models import Client
import uuid

def increment_invoice_number():
    """
    Increments invoice number from previous number. can be used
    to format the invoice number as desired
    """
    #last_invoice= Invoice.objects.filter(Business).order_by('inv_no')
    last_invoice = Invoice.objects.all().order_by('inv_no').last()
    if not last_invoice:
        return 'INV0001'
    invoice_no=last_invoice.inv_no
    invoice_int = int(invoice_no.split('INV')[-1])
    width = 4
    new_invoice_int=invoice_int+1
    formatted = (width - len(str(new_invoice_int))) * "0" + str(new_invoice_int)
    new_invoice_no = 'INV' + str(formatted)
    return new_invoice_no
def increment_receipt_number():
    """
    Increments receipt number from previous number. can be used
    to format the receipt number as desired
    """
    #last_invoice= Invoice.objects.filter(Business).order_by('inv_no')
    last_receipt = Receipt.objects.all().order_by('recpt_no').last()
    if not last_receipt:
        return 'RCTP0001'
    receipt_no=last_receipt.recpt_no
    receipt_int = int(receipt_no.split('RCTP')[-1])
    width = 4
    new_receipt_int=receipt_int+1
    formatted = (width - len(str(new_receipt_int))) * "0" + str(new_receipt_int)
    new_receipt_no = 'RCTP' + str(formatted)
    return new_receipt_no

class Service(BusinessAwareModel):
    """
    what servicces does the company offer
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    service_name = models.CharField(_('Service Name'), max_length=30, blank=False)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

class Client_Service(BusinessAwareModel):
    """
    Cost of a service depends on the client category
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    monthly_charge = models.CharField(_('Cost of Service Per Month'), max_length=10, blank=False)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

class Invoice(BusinessAwareModel):
    """
    Invoices are generated monthly
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    inv_no =models.CharField(_("Invoice Number"), max_length=50, default=increment_invoice_number, unique=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    invoice_amount = models.CharField(_('Amount Invoiced'), max_length=10, blank=False)
    invoice_balance = models.CharField(_('Invoice Balance'), max_length=10, blank=False)
    extra_charges = models.CharField(_("Extra charges"), max_length=10,blank=True )
    invoice_date =models.DateField(_("Invoice Date"), auto_now_add=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

class Payment_Method(BusinessAwareModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    method_name = models.CharField(_("Method Name"), max_length=20)
class Receipt(BusinessAwareModel):
    """
    Issued once an invoice is paid
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    recpt_no =models.CharField(_("Invoice Number"), max_length=50, default=increment_receipt_number, unique=True)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)    
    amount_paid = models.CharField(_('Receipt Amount'), max_length=20, blank=False)
    balance = models.CharField(_('Balance'), max_length=20, blank=True)
    receipt_date =models.DateField(_("Receipt Date"), auto_now_add=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
