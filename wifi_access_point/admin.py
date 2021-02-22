from django.contrib import admin
from wifi_access_point.models import AccessPointScan


class AccessPointScanAdmin(admin.ModelAdmin):
    list_display = (
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
        "date_created",
    )


admin.site.register(AccessPointScan, AccessPointScanAdmin)
