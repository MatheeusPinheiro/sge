from django.urls import path
from inflows import views

urlpatterns = [
    path("inflows/list/", views.InflowListViews.as_view(), name="inflow_list"),
    path("inflows/create/", views.InflowCreateView.as_view(), name="inflow_create"),
    path("inflows/<int:pk>/detail/", views.InflowDetailView.as_view(), name="inflow_detail"),
 
]