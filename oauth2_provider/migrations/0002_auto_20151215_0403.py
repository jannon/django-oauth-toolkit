# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('oauth2_provider', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesstoken',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, blank=True),
        ),
    ]
