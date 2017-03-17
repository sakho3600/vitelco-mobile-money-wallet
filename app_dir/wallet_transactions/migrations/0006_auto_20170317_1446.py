# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 11:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet_transactions', '0005_auto_20170317_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='state',
            field=models.CharField(choices=[(b'received', b'received'), (b'in_progress', b'in_progress'), (b'completed', b'completed'), (b'failed', b'failed')], default=b'received', max_length=20),
        ),
    ]