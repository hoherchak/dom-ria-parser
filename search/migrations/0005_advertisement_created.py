# Generated by Django 2.2.3 on 2019-07-18 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0004_auto_20190718_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='created',
            field=models.DateTimeField(default=None, blank=True, null=True),
            preserve_default=False,
        ),
    ]
