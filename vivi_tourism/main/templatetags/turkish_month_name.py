from django import template
from django.utils.translation import gettext as _
from datetime import datetime

register = template.Library()

@register.filter
def turkish_month_name(date):
    print(date.month - 1)
    print(type(date))
    # Define Turkish month names
    turkish_month_names = [
        _('Ocak'), _('Şubat'), _('Mart'), _('Nisan'), _('Mayıs'), _('Haziran'),
        _('Temmuz'), _('Ağustos'), _('Eylül'), _('Ekim'), _('Kasım'), _('Aralık')
    ]

    # Get the month index and return the corresponding Turkish month name
    return turkish_month_names[date.month - 1]
