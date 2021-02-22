import pytest
from django.test import TestCase, RequestFactory
from rest_framework.utils import json

from wifi_access_point.views import *  # noqa


@pytest.mark.django_db
class TestAccessPointScanApi(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.access_point_scan = AccessPointScan.objects.create(
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

    def test_get_api_all_wifi_access_point_scan_list(self):
        request = self.factory.get("/api/v1/apscan/all/")
        view = ListAllAccessPointScanAPIView.as_view()
        response = view(request)

        assert response.data["count"] == 1
        assert response.status_code == status.HTTP_200_OK
        assert self.access_point_scan.id == response.data["apscan_data"][0]["id"]

    def test_get_api_wifi_access_point_scan_retrieve(self):
        pk = self.access_point_scan.id
        request = self.factory.get("/api/v1/apscan/{}/retrieve/".format(pk))

        view = RetrieveAccessPointScanAPIView.as_view()
        response = view(request, pk=pk)

        assert pk == response.data["id"]
        assert response.status_code == status.HTTP_200_OK

    def test_delete_api_wifi_access_point_scan_single(self):
        pk = self.access_point_scan.id
        request = self.factory.delete("/api/v1/apscan/{}/delete/".format(pk))

        view = DeleteAccessPointScanAPIView.as_view()
        response = view(request, pk=pk)

        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_post_api_wifi_access_point_scan_with_valid_data(self):
        content_type = "application/json"
        data = {
            "band": "2.4",
            "bssid": "84:78:ac:b9:76:19",
            "channel": "1",
            "frequency": 2412,
            "rates": "6.5 - 270.0 Mbps",
            "rssi": -71,
            "security": "wpa-eap",
            "ssid": "1 Telkom Connect",
            "timestamp": 1522886948.0,
            "vendor": "Cisco Systems, Inc",
            "width": "20",
        }

        request = self.factory.post(
            "/api/v1/apscan/add/", json.dumps(data), content_type=content_type
        )
        view = CreateAccessPointScanAPIView.as_view()
        response = view(request)

        assert "accuracy" in response.data
        assert "location" in response.data
        assert "lat" in response.data["location"]
        assert "lng" in response.data["location"]
        assert response.status_code == status.HTTP_201_CREATED

    def test_post_api_wifi_access_point_scan_with_invalid_data(self):
        content_type = "application/json"
        data = dict()

        request = self.factory.post(
            "/api/v1/apscan/add/", json.dumps(data), content_type=content_type
        )
        view = CreateAccessPointScanAPIView.as_view()
        response = view(request)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "This field is required." in response.data["bssid"]

    def test_update_api_wifi_access_point_scan_with_invalid_pk(self):
        pk = 0
        content_type = "application/json"
        data = {
            "band": "5.4",
            "bssid": "84:78:ac:b9:76:19",
            "channel": "600",
        }

        request = self.factory.put(
            "api/v1/apscan/{}/edit".format(pk),
            json.dumps(data),
            content_type=content_type,
        )
        view = UpdateAccessPointScanAPIView.as_view()
        response = view(request, pk=pk)

        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_update_api_wifi_access_point_scan_with_valid_pk(self):
        apscan = self.access_point_scan
        content_type = "application/json"
        data = {"band": "5.4", "channel": "600"}

        request = self.factory.put(
            "api/v1/apscan/{}/edit".format(apscan.id),
            json.dumps(data),
            content_type=content_type,
        )
        view = UpdateAccessPointScanAPIView.as_view()
        response = view(request, pk=apscan.id)

        assert response.data["band"] == float(data["band"])
        assert response.data["channel"] == int(data["channel"])
        assert response.status_code == status.HTTP_200_OK
