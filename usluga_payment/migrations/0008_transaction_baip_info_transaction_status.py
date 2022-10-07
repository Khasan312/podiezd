# Generated by Django 4.1.1 on 2022-10-07 03:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usluga_payment', '0007_alter_baipinfo_options_baipinfo_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='baip_info',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='usluga_payment.baipinfo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='status',
            field=models.CharField(choices=[('received', 'RECEIVED'), ('cancelled', 'CANCELLED'), ('waiting', 'WAITING')], default='waiting', max_length=32),
        ),
    ]
