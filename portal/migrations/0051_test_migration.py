# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings

def insert_test_user():
    teacher_user = User.objects.create(
        username='isJenkinsWorking',
        first_name='isJenkinsWorking',
        last_name='isJenkinsWorking',
        email='isJenkinsWorking@codeforlife.com',
        password=make_password(os.getenv('ADMIN_PASSWORD', 'Password1')))

class Migration(migrations.Migration):
    dependencies = [
        ('portal', '0050_refactor_emailverifications_2'),
    ]

    operations = [
        migrations.RunPython(
            code=insert_test_user,
        ),
    ]
