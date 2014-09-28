# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='officerprofile',
            name='photo',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='funny_picture',
            field=models.ImageField(default='/profile_images/spock.jpg', upload_to='profile_images'),
            preserve_default=True,
        ),
    ]
