# Generated by Django 4.0.4 on 2022-06-27 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_alter_category_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='monthly_charge',
            field=models.CharField(blank=True, max_length=15, verbose_name='Monthy Charge'),
        ),
    ]
