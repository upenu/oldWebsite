# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20150327_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='grad_year',
            field=models.CharField(verbose_name='When are you graduating | When did you graduate?', choices=[('95', '1995'), ('96', '1996'), ('97', '1997'), ('98', '1998'), ('99', '1999'), ('00', '2000'), ('01', '2001'), ('02', '2002'), ('03', '2003'), ('04', '2004'), ('05', '2005'), ('06', '2006'), ('07', '2007'), ('08', '2008'), ('09', '2009'), ('10', '2010'), ('11', '2011'), ('12', '2012'), ('13', '2013'), ('14', '2014'), ('15', '2015'), ('16', '2016'), ('17', '2017'), ('18', '2018')], max_length=4, default='15'),
        ),
    ]
