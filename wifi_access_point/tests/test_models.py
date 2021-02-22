import pytest

from wifi_access_point.models import AccessPointScan


@pytest.mark.django_db
class TestAccessPointScanModelObjectClass:
    def test_access_point_scan_model_object_creation(self):
        new_access_point_scan = AccessPointScan.objects.create(
            band="2.4",
            bssid="84:78:ac:b9:76:19",
            channel="1",
            frequency=2412,
            rates="6.5 - 270.0 Mbps",
            rssi=-71,
            security="wpa-eap",
            ssid="1 Telkom Connect",
            timestamp=1522886948.0,
            vendor="Cisco Systems, Inc",
            width="20",
        )

        assert new_access_point_scan.bssid == "84:78:ac:b9:76:19"
        assert new_access_point_scan.channel == "1"
        assert new_access_point_scan.frequency == 2412
