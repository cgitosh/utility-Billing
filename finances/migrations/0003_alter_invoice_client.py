# Generated by Django 4.0.4 on 2022-06-27 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_category_monthly_charge'),
        ('finances', '0002_remove_invoice_client_service_invoice_client_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.client'),
        ),
    ]
