# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import snippets.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('info', models.TextField()),
                ('rating', models.DecimalField(max_digits=4, decimal_places=2)),
                ('score', models.DecimalField(max_digits=4, decimal_places=2)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=snippets.models.scramble_uploaded_filename)),
                ('owner', models.ForeignKey(related_name='profiles', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100, blank=True, default='')),
                ('body', models.TextField()),
                ('owner', models.ForeignKey(related_name='snippets', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='SocialNetwork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100, blank=True, default='')),
                ('type', models.CharField(max_length=100, blank=True, default='fb')),
                ('url', models.CharField(max_length=100, blank=True, default='')),
                ('owner', models.ForeignKey(related_name='socialnetworks', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('type',),
            },
        ),
        migrations.CreateModel(
            name='TShirt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('message', models.CharField(max_length=100, blank=True, default='')),
                ('color', models.TextField()),
                ('size', models.TextField()),
                ('code', models.TextField()),
                ('owner', models.ForeignKey(related_name='tshirts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
