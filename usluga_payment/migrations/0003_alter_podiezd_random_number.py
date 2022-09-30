# Generated by Django 4.1.1 on 2022-09-29 04:01

from django.db import migrations, models
import usluga_payment.utils


class Migration(migrations.Migration):

    dependencies = [
        ('usluga_payment', '0002_alter_podiezd_random_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podiezd',
            name='random_number',
            field=models.CharField(blank=True, default=usluga_payment.utils.create_new_ref_number, editable=False, max_length=20, unique=True),
        ),
    ]
