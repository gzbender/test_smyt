# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_smyt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64, verbose_name='\u0413\u0440\u0443\u043f\u043f\u0430 \u0442\u043e\u0432\u0430\u0440\u0430')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0442\u043e\u0432\u0430\u0440\u0430')),
                ('price', models.DecimalField(verbose_name='\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u0435\u0434\u0438\u043d\u0438\u0446\u044b, \u0440\u0443\u0431.', max_digits=10, decimal_places=2)),
                ('category', models.ForeignKey(verbose_name='\u0413\u0440\u0443\u043f\u043f\u0430', to='test_smyt.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
