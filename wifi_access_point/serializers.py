from rest_framework import serializers

from wifi_access_point.models import AccessPointScan


class CreateAccessPointScanSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessPointScan
        fields = (
            "id",
            "band",
            "bssid",
            "channel",
            "frequency",
            "rates",
            "rssi",
            "security",
            "ssid",
            "timestamp",
            "vendor",
            "width",
        )


class DetailAccessPointScanSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessPointScan
        fields = (
            "id",
            "band",
            "bssid",
            "channel",
            "frequency",
            "rates",
            "rssi",
            "security",
            "ssid",
            "timestamp",
            "vendor",
            "width",
            "geolocation_data",
            "has_geolocation_data",
        )
