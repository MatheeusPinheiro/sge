from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from outflows.models import Outflow
from outflows.forms import OutflowForm
from app import metrics


class OutflowListViews(ListView):
    model = Outflow
    template_name = "outflow_list.html"
    context_object_name = "outflows"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        product = self.request.GET.get("product")

        if product:
            queryset = queryset.filter(product__title__icontains=product)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sales_metrics'] = metrics.get_sales_metrics()
        return context
    

class OutflowCreateView(CreateView):
    model = OutflowForm
    template_name = "outflow_create.html"
    form_class = OutflowForm
    success_url = reverse_lazy("outflow_list")


class OutflowDetailView(DetailView):
    model = Outflow
    template_name = "outflow_detail.html"


