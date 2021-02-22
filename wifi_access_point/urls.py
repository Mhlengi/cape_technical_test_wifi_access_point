from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from wifi_access_point import views

urlpatterns = [
    path("all/", views.ListAllAccessPointScanAPIView.as_view()),
    path("add/", views.CreateAccessPointScanAPIView.as_view()),
    path("<int:pk>/edit/", views.UpdateAccessPointScanAPIView.as_view()),
    path("<int:pk>/delete/", views.DeleteAccessPointScanAPIView.as_view()),
    path("<int:pk>/retrieve/", views.RetrieveAccessPointScanAPIView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
