from django.db.models import Q
from django_filters import filterset

from core import models


class NumberInFilter(filterset.BaseInFilter, filterset.NumberFilter):
    pass


class CharInFilter(filterset.BaseInFilter, filterset.CharFilter):
    pass


class NumberRangeFilter(filterset.BaseRangeFilter, filterset.NumberFilter):
    pass


class EmployeeFilter(filterset.FilterSet):
    name = filterset.CharFilter(lookup_expr='icontains')
    start_salary = filterset.NumberFilter(lookup_expr='gte', field_name='salary')
    end_salary = filterset.NumberFilter(lookup_expr='lte', field_name='salary')

    salary_range = NumberRangeFilter(field_name='salary', lookup_expr='range')
    salary_in = NumberInFilter(field_name='salary', lookup_expr='in')
    gender_in = CharInFilter(field_name='gender', lookup_expr='in')

    name_or_department = filterset.CharFilter(method='filter_name_or_department')

    @staticmethod
    def filter_name_or_department(queryset, name, value):
        return queryset.filter(
            Q(name__icontains=value) | Q(department__name__icontains=value)
        )

    class Meta:
        model = models.Employee
        fields = ['name', 'start_salary', 'end_salary',
                  'salary_range', 'salary_in', 'gender_in',
                  'name_or_department']