from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.utils.translation import gettext_lazy as _
from accounts.models import BusinessAwareModel,User
import uuid

# Create your models here.

class category(BusinessAwareModel):
    """
    A client can be single residential, Multidweller residential (apartments) or commercial
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category_name = models.CharField(_('Category Name'), max_length=50, blank=False)
    monthly_charge = models.CharField(_('Monthy Charge'), max_length=15, blank=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

class Client(BusinessAwareModel):
    """
    A client receives services from a business at a cost
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    house_no=models.CharField(_("House No"),max_length=15, blank=True)
    category=models.ForeignKey(category, on_delete=models.CASCADE)
    first_name = models.CharField(_('First Name'), max_length=30, blank=False)
    last_name = models.CharField(_('Last Name'), max_length=30, blank=True)
    mobile_no = models.CharField(_('Mobile Contact'), max_length=15, blank=False, unique=True)
    address=models.CharField(_("Street Address"),blank=True, max_length=200)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('client')
        verbose_name_plural = _('clients')

    def __str__(self):
        return self.first_name





