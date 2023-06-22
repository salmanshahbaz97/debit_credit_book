from django_filters.rest_framework import FilterSet
from .models import Sales


class SalesFilter(FilterSet):
    class Meta:
        model = Sales
        fields = {
            'amount': ['lt', 'gt'],
            'date': ['lt', 'gt'],
        }
