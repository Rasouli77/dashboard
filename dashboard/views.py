from django.shortcuts import render
from .models import Invoice
from django.db.models import Sum
from django.db.models.functions import TruncDate
import json

# Create your views here.
def highchart(request):
    queryset = (
        Invoice.objects.
        annotate(day=TruncDate('date_created')).
        values('day').
        annotate(total=Sum('total_amount')).
        order_by('day')
    )

    days = [str(row['day']) for row in queryset]
    totals = [float(row['total']) for row in queryset]


    return render(request, 'base.html', {"days": json.dumps(days), "totals": json.dumps(totals)})