# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 06:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet_transactions', '0017_auto_20170322_0848'),
    ]

    operations = [
        migrations.RenameField(
            model_name='debitmandate',
            old_name='frequecy_type',
            new_name='frequency_type',
        ),
    ]