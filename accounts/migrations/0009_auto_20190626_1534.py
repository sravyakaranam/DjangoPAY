# Generated by Django 2.2.2 on 2019-06-26 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20190626_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='AccountUser',
            field=models.CharField(help_text='user name', max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
