# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('sender', models.TextField()),
                ('receiver', models.TextField()),
                ('subject', models.TextField()),
                ('body', models.TextField()),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
