from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="نام")
    price = models.CharField(max_length=255, verbose_name="قیمت")
    discount_price = models.CharField(max_length=255, verbose_name="قیمت با تخفیف")
    stock = models.PositiveIntegerField(verbose_name="موجودی")
    status = models.CharField(max_length=255, verbose_name="وضعیت")
    product_code = models.CharField(max_length=255, verbose_name="کد محصول")
    amount_sold = models.CharField(
        max_length=255, verbose_name="جمع مبلغ فروش", null=True
    )
    quantity_sold = models.PositiveIntegerField(
        verbose_name="تعداد اقلام فروش رفته", null=True
    )
    date_created = models.DateField(verbose_name="تاریخ ساخت")

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصول"


class Customer(models.Model):
    name = models.CharField(max_length=255, verbose_name="نام")
    phone_number = models.CharField(max_length=11, verbose_name="شماره تلفن")
    rfm = models.CharField(max_length=255, verbose_name="RFM", null=True)
    address = models.TextField(verbose_name="آدرس", null=True)
    location_latitude = models.CharField(
        max_length=255, verbose_name="عرض جغرافیایی", null=True
    )
    location_longitude = models.CharField(
        max_length=255, verbose_name="طول جغرافیایی", null=True
    )
    city = models.CharField(max_length=255, verbose_name="شهر", null=True)
    amount_bought = models.CharField(
        max_length=255, verbose_name="مبلغ کل خرید ها", null=True
    )
    invoice_quantity = models.PositiveIntegerField(
        verbose_name="تعداد فاکتور", null=True
    )
    invoice_item_quantity = models.PositiveIntegerField(
        verbose_name="تعداد اقلام کل فاکتور ها", null=True
    )
    last_bought = models.DateField(verbose_name="تاریخ آخرین خرید", null=True)
    date_created = models.DateField(verbose_name="تاریخ ساخت")

    class Meta:
        verbose_name = "مشتری"
        verbose_name_plural = "مشتری"


class Invoice(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, verbose_name="مشتری"
    )
    total_amount = models.CharField(max_length=255, verbose_name="مبلغ کل")
    total_quantity = models.PositiveIntegerField(verbose_name="تعداد کل اقلام فاکتور")
    date_created = models.DateField(verbose_name="تاریخ ساخت")
    status = models.BooleanField(verbose_name="وضعیت سفارش")
    branch = models.CharField(max_length=255, verbose_name="شعبه", null=True)

    class Meta:
        verbose_name = "فاکنور"
        verbose_name_plural = "فاکتور"


class InvoiceItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="محصول")
    invoice = models.ForeignKey(
        Invoice, on_delete=models.CASCADE, verbose_name="فاکتور"
    )
    quantity = models.PositiveIntegerField(verbose_name="تعداد")
    price = models.CharField(max_length=255, verbose_name="قیمت")
    date_created = models.DateField(verbose_name="تاریخ ساخت")

    class Meta:
        verbose_name = "اقلام فاکتور"
        verbose_name_plural = "اقلام فاکتور"
