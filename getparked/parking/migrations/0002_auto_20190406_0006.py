# Generated by Django 2.1.7 on 2019-04-06 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]