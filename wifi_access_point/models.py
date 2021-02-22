from django.db import models


class AccessPointScan(models.Model):
    band = models.FloatField(max_length=10, default=0)
    bssid = models.CharField(max_length=250)
    channel = models.IntegerField(null=True)
    frequency = models.IntegerField(default=0)
    rates = models.CharField(max_length=250, null=True)
    rssi = models.IntegerField(default=0)
    security = models.CharField(max_length=250, null=True)
    ssid = models.CharField(max_length=250, null=True)
    timestamp = models.IntegerField(null=True)
    vendor = models.CharField(max_length=250, null=True)
    width = models.IntegerField(null=True)
    geolocation_data = models.JSONField(default=dict)
    has_geolocation_data = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return str(self.bssid)
