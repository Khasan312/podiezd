# Generated by Django 4.1.1 on 2022-10-07 04:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("usluga_payment", "0008_transaction_baip_info_transaction_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="baip_info",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="usluga_payment.baipinfo",
            ),
        ),
    ]