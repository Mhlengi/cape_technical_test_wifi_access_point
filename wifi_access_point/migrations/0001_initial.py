# Generated by Django 3.1.6 on 2021-02-21 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessPointScan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('band', models.FloatField(default=0, max_length=10)),
                ('bssid', models.CharField(max_length=250)),
                ('channel', models.IntegerField(null=True)),
                ('frequency', models.IntegerField(default=0)),
                ('rates', models.CharField(max_length=250, null=True)),
                ('rssi', models.IntegerField(default=0)),
                ('security', models.CharField(max_length=250, null=True)),
                ('ssid', models.CharField(max_length=250, null=True)),
                ('timestamp', models.IntegerField(null=True)),
                ('vendor', models.CharField(max_length=250, null=True)),
                ('width', models.IntegerField(null=True)),
                ('geolocation_data', models.JSONField(default=dict)),
                ('has_geolocation_data', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
