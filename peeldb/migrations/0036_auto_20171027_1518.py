# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-27 15:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("peeldb", "0035_user_registered_from"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="registered_from",
            field=models.CharField(
                choices=[
                    ("Email", "Email"),
                    ("Social", "Social"),
                    ("ResumePool", "ResumePool"),
                    ("Resume", "Resume"),
                    ("Careers", "Careers"),
                ],
                default="",
                max_length=15,
            ),
        ),
    ]
