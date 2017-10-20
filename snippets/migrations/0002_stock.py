# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('color', models.TextField()),
                ('size', models.TextField()),
                ('code', models.TextField()),
                ('pin', models.TextField()),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
