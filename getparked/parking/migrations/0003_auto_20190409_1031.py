# Generated by Django 2.2 on 2019-04-09 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0002_auto_20190409_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bay',
            name='notes',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
