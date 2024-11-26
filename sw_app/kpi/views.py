from django.shortcuts import render
from rest_framework import generics, response,status
from rest_framework.views import APIView
from .models import Kpi , KpiAssetLink
from .serializers import KpiSerializer, KpiAssetSerializer
from drf_spectacular.utils import extend_schema

@extend_schema(
    tags=["KPI"],
    description="Retrieve a list of all KPIs or create a new KPI.",
)
class KpiListCreate(generics.ListCreateAPIView):
    queryset = Kpi.objects.all()
    serializer_class = KpiSerializer


@extend_schema(
    tags=["KPIAsset"],
    description="Retrieve a certain kpi to view, delete or update it with its id",
)
class KpiRetUpdatetDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kpi.objects.all()
    serializer_class = KpiSerializer
    lookup_field = "pk"


@extend_schema(
    tags=["KPIAsset"],
    description="Retrieve a list of all AssetsID, KPI_ID and their result or create a new record.",
)
class KpiAssetCreate(generics.ListCreateAPIView):
    queryset = KpiAssetLink.objects.all()
    serializer_class = KpiAssetSerializer

@extend_schema(
    tags=["KPIAsset"],
    description="Retrieve a certain AssetsID, KPI_ID and their result , update or delete one by the id",
)
class KpiAssetRetUpdatetDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = KpiAssetLink.objects.all()
    serializer_class = KpiAssetSerializer
    lookup_field = "pk"

@extend_schema(
    tags=["KPIAsset"],
    description="Delete All records",
)
class KpiAssetDestroyAll(APIView):

    def delete(self, request, *args, **kwargs):
        count, _ = KpiAssetLink.objects.all().delete()
        return response.Response(
            {"message": f"Deleted {count} records successfully."},
            status=status.HTTP_200_OK
        )