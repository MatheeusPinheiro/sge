from django.urls import path
from outflows import views

urlpatterns = [
    path("outflows/list/", views.OutflowListViews.as_view(), name="outflow_list"),
    path("outflows/create/", views.OutflowCreateView.as_view(), name="outflow_create"),
    path("outflows/<int:pk>/detail/", views.OutflowDetailView.as_view(), name="outflow_detail"),
 
]