# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('test_smyt', '0002_category_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField()),
                ('status', models.SmallIntegerField(choices=[(3, '\u041d\u0435 \u043f\u0440\u043e\u0434\u0430\u043d'), (7, '\u041f\u0440\u043e\u0434\u0430\u043d'), (5, '\u0420\u0435\u0437\u0435\u0440\u0432')])),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone', models.CharField(max_length=255)),
                ('users', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
            ],
        ),
    ]
