# Generated by Django 2.1.7 on 2019-04-06 00:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0004_auto_20190406_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='bay_id',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='parking.ReservedBay'),
        ),
    ]
