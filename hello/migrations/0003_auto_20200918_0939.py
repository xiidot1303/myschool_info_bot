# Generated by Django 3.0.8 on 2020-09-18 04:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_auto_20200918_0937'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='drafts',
            new_name='dt',
        ),
        migrations.RenameField(
            model_name='dt',
            old_name='words',
            new_name='w',
        ),
    ]
