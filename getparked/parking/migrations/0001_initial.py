# Generated by Django 2.1.7 on 2019-04-04 08:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Lot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=300, unique=True)),
                ('bays', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LotDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.FloatField()),
                ('lot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='day', to='parking.Lot')),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking', to='parking.Customer'),
        ),
        migrations.AddField(
            model_name='booking',
            name='days',
            field=models.ManyToManyField(related_name='booking', to='parking.LotDay'),
        ),
    ]
