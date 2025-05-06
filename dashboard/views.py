from django.shortcuts import render
from .models import Invoice
from django.db.models import Sum
from django.db.models.functions import TruncDate
from datetime import datetime
import json
import jdatetime

def jalali_to_gregorian(date_str: str):
    try:
        jyear, jmonth, jday = map(int, date_str.split("-"))
        gregorian_date = jdatetime.date(jyear, jmonth, jday).togregorian()
        return gregorian_date
    except Exception as e:
        print(e)
        return None

# Create your views here.
def highchart(request):
    queryset = (
        Invoice.objects.
        annotate(day=TruncDate('date_created')).
        values('day').
        annotate(total=Sum('total_amount')).
        order_by('day')
    )
    start_date_str = str(jalali_to_gregorian(request.GET.get("start-date")))
    end_date_str = str(jalali_to_gregorian(request.GET.get("end-date")))
    if start_date_str and end_date_str:
        start_date = 0
        end_date = 0
        try:
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()
            queryset = queryset.filter(day__range=(start_date, end_date))
        except Exception as e:
            print(e)

    days = [str(row['day']) for row in queryset]
    totals = [float(row['total']) for row in queryset]


    return render(request, 'base.html', {"days": json.dumps(days), "totals": json.dumps(totals)})