# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-11 22:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pinax_stripe', '0013_charge_outcome'),
    ]

    operations = [
        migrations.AddField(
            model_name='charge',
            name='stripe_account_hc',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='pinax_stripe.Account'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='stripe_account_hc',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='pinax_stripe.Account'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='stripe_account_hc',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='pinax_stripe.Account'),
        ),
    ]
