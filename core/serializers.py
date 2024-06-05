from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers

from core import models


class StateSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = models.State
        fields = '__all__'


class CitySerializer(FlexFieldsModelSerializer):
    class Meta:
        model = models.City
        fields = '__all__'

        expandable_fields = {
            'state': ('core.StateSerializer', {
                'fields': ['id', 'name']
            })
        }


class ZoneSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = models.Zone
        fields = '__all__'


class DistrictSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = models.District
        fields = '__all__'


class MaritalStatusSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = models.MaritalStatus
        fields = '__all__'


class CustomerSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = models.Customer
        fields = '__all__'


class BranchSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = models.Branch
        fields = '__all__'


class DepartmentSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = models.Department
        fields = '__all__'


class EmployeeSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = models.Employee
        fields = '__all__'


class SaleSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = models.Sale
        fields = '__all__'


class SaleItemSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = models.SaleItem
        fields = '__all__'


class SupplierSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = models.Supplier
        fields = '__all__'


class ProductGroupSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = models.ProductGroup
        fields = '__all__'


class ProductSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'