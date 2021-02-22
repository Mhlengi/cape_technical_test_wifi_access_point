import requests
from django.http import Http404

from config import GOOGLE_API_KEY

BASE_URL = "https://www.googleapis.com/geolocation/v1/geolocate?key="
GOOGLE_MAPS_API_URL = "{}{}".format(BASE_URL, GOOGLE_API_KEY)


def geolocation_search(data):
    """

    @param data:
    @return:
    """
    if "bssid" not in data:
        raise Http404

    params = {
        "macAddress": data["bssid"],
        "signalStrength": data["rssi"],
        "age": int(data["timestamp"]),
        "channel": int(data["channel"]),
        "signalToNoiseRatio": data["frequency"],
    }

    req = requests.post(GOOGLE_MAPS_API_URL, params=params)
    status = req.status_code
    payload = req.json()

    return status, payload
