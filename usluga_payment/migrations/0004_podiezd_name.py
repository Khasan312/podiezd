# Generated by Django 4.1.1 on 2022-10-06 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("usluga_payment", "0003_alter_podiezd_random_number"),
    ]

    operations = [
        migrations.AddField(
            model_name="podiezd",
            name="name",
            field=models.CharField(default=1, max_length=164),
            preserve_default=False,
        ),
    ]