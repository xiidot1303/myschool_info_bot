# Generated by Django 3.0.8 on 2020-09-18 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0004_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='group',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='surname',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='group',
        ),
    ]