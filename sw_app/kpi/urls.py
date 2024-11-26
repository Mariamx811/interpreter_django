from django.urls import path
from . import views

urlpatterns = [
    path("kpi/", views.KpiListCreate.as_view(),name="kpi-view-create"),
    path("kpiasset/",views.KpiAssetCreate.as_view(),name="kpi-asset"),
    path("kpiasset/<int:pk>",views.KpiAssetRetUpdatetDelete.as_view(),name="kpi-asset-update"),
    path("kpi/<int:pk>",views.KpiRetUpdatetDelete.as_view(),name="kpi-update"),
    path("kpiasset/delete",views.KpiAssetDestroyAll.as_view(),name="kpi-delete")

]