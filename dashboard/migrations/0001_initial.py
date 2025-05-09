# Generated by Django 5.0 on 2025-05-03 14:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="نام")),
                (
                    "phone_number",
                    models.CharField(max_length=11, verbose_name="شماره تلفن"),
                ),
                (
                    "rfm",
                    models.CharField(max_length=255, null=True, verbose_name="RFM"),
                ),
                ("address", models.TextField(null=True, verbose_name="آدرس")),
                (
                    "location_latitude",
                    models.CharField(
                        max_length=255, null=True, verbose_name="عرض جغرافیایی"
                    ),
                ),
                (
                    "location_longitude",
                    models.CharField(
                        max_length=255, null=True, verbose_name="طول جغرافیایی"
                    ),
                ),
                (
                    "city",
                    models.CharField(max_length=255, null=True, verbose_name="شهر"),
                ),
                (
                    "amount_bought",
                    models.CharField(
                        max_length=255, null=True, verbose_name="مبلغ کل خرید ها"
                    ),
                ),
                (
                    "invoice_quantity",
                    models.PositiveIntegerField(null=True, verbose_name="تعداد فاکتور"),
                ),
                (
                    "invoice_item_quantity",
                    models.PositiveIntegerField(
                        null=True, verbose_name="تعداد اقلام کل فاکتور ها"
                    ),
                ),
                (
                    "last_bought",
                    models.DateField(null=True, verbose_name="تاریخ آخرین خرید"),
                ),
                ("date_created", models.DateField(verbose_name="تاریخ ساخت")),
            ],
            options={
                "verbose_name": "مشتری",
                "verbose_name_plural": "مشتری",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="نام")),
                ("price", models.CharField(max_length=255, verbose_name="قیمت")),
                (
                    "discount_price",
                    models.CharField(max_length=255, verbose_name="قیمت با تخفیف"),
                ),
                ("stock", models.PositiveIntegerField(verbose_name="موجودی")),
                ("status", models.CharField(max_length=255, verbose_name="وضعیت")),
                (
                    "product_code",
                    models.CharField(max_length=255, verbose_name="کد محصول"),
                ),
                (
                    "amount_sold",
                    models.CharField(
                        max_length=255, null=True, verbose_name="جمع مبلغ فروش"
                    ),
                ),
                (
                    "quantity_sold",
                    models.PositiveIntegerField(
                        null=True, verbose_name="تعداد اقلام فروش رفته"
                    ),
                ),
                ("date_created", models.DateField(verbose_name="تاریخ ساخت")),
            ],
            options={
                "verbose_name": "محصول",
                "verbose_name_plural": "محصول",
            },
        ),
        migrations.CreateModel(
            name="Invoice",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "total_amount",
                    models.CharField(max_length=255, verbose_name="مبلغ کل"),
                ),
                (
                    "total_quantity",
                    models.PositiveIntegerField(verbose_name="تعداد کل اقلام فاکتور"),
                ),
                ("date_created", models.DateField(verbose_name="تاریخ ساخت")),
                ("status", models.BooleanField(verbose_name="وضعیت سفارش")),
                (
                    "branch",
                    models.CharField(max_length=255, null=True, verbose_name="شعبه"),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dashboard.customer",
                        verbose_name="مشتری",
                    ),
                ),
            ],
            options={
                "verbose_name": "فاکنور",
                "verbose_name_plural": "فاکتور",
            },
        ),
        migrations.CreateModel(
            name="InvoiceItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.PositiveIntegerField(verbose_name="تعداد")),
                ("price", models.CharField(max_length=255, verbose_name="قیمت")),
                ("date_created", models.DateField(verbose_name="تاریخ ساخت")),
                (
                    "invoice",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dashboard.invoice",
                        verbose_name="فاکتور",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dashboard.product",
                        verbose_name="محصول",
                    ),
                ),
            ],
            options={
                "verbose_name": "اقلام فاکتور",
                "verbose_name_plural": "اقلام فاکتور",
            },
        ),
    ]
