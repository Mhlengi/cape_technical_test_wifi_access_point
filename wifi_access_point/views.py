from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from wifi_access_point.geolocation_search import geolocation_search
from wifi_access_point.models import AccessPointScan
from wifi_access_point.serializers import (
    CreateAccessPointScanSerializer,
    DetailAccessPointScanSerializer,
)


def get_object(_class, pk):
    """

    @param _class:
    @param pk:
    @return:
    """

    try:
        return _class.objects.get(pk=pk)
    except _class.DoesNotExist:
        raise Http404


def clean_lat_lng(data):
    """

    @param data:
    @return:
    """
    if "location" and "accuracy" not in data:
        return dict()

    if "lat" and "lng" not in data["location"]:
        return dict()

    data["location"]["lat"] = float("{:.1f}".format(data["location"]["lat"]))
    data["location"]["lng"] = float("{:.1f}".format(data["location"]["lng"]))
    data["accuracy"] = float("{:.1f}".format(data["accuracy"]))

    return data


class ListAllAccessPointScanAPIView(APIView):
    """
    List all WIFI access point scan.
    GET http Method.
    """

    # list all WIFI access point scan
    def get(self, request):
        access_points = AccessPointScan.objects.all().order_by("-date_created")
        serializer = DetailAccessPointScanSerializer(access_points, many=True)
        data = {"apscan_data": serializer.data, "count": access_points.count()}
        return Response(data)


class CreateAccessPointScanAPIView(APIView):
    """
    Create a new WIFI access point scan.
    POST http Method.
    """

    def post(self, request):
        serializer = CreateAccessPointScanSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            # Create new or Get existing WIFI access point scan on DB
            access_point, created = AccessPointScan.objects.get_or_create(
                bssid=data["bssid"],
                band=data["band"],
                channel=data["channel"],
                frequency=data["frequency"],
                rates=data["rates"],
                rssi=data["rssi"],
                security=data["security"],
                ssid=data["ssid"],
                timestamp=data["timestamp"],
                vendor=data["vendor"],
                width=data["width"],
            )
            if created:
                # If new WIFI access point scan created, perform geolocation-search lat and lng
                # location.
                search_data = geolocation_search(data)
                access_point.geolocation_data = search_data[1]
                access_point.has_geolocation_data = True
            else:
                # If WIFI access point scan already exist, but no geolocation lat and lng,
                # then update by perform geolocation-search lat and lng location.
                if not access_point.has_geolocation_data:
                    search_data = geolocation_search(data)
                    access_point.geolocation_data = search_data[1]
                    access_point.has_geolocation_data = True
            access_point.save()
            data = clean_lat_lng(access_point.geolocation_data)
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RetrieveAccessPointScanAPIView(APIView):
    """
    Get a single WIFI access point scan.
    GET http Method.
    """

    def get(self, request, pk):
        access_point = get_object(AccessPointScan, pk)
        serializer = DetailAccessPointScanSerializer(access_point)
        return Response(serializer.data)


class UpdateAccessPointScanAPIView(APIView):
    """
    Update a single WIFI access point scan.
    UPDATE http Method.
    """

    def put(self, request, pk):
        data = request.data
        access_point = get_object(AccessPointScan, pk)
        data["bssid"] = access_point.bssid if "bssid" not in data else data["bssid"]
        serializer = DetailAccessPointScanSerializer(access_point, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteAccessPointScanAPIView(APIView):
    """
    Delete a single WIFI access point scan.
    DELETE http Method.
    """

    def delete(self, request, pk):
        access_point = get_object(AccessPointScan, pk)
        access_point.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
