import django_filters
from apps.lessons.models import Schedule, Date


class ScheduleFilter(django_filters.FilterSet):
    date = django_filters.DateFilter(field_name="date", lookup_expr="exact", label="Дата")

    class Meta:
        model = Date
        fields = ('date',)
