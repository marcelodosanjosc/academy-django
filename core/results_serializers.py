from rest_framework import serializers


class EmployeeCountByDepartmentSerializer(serializers.Serializer):
    department = serializers.CharField()
    qty = serializers.IntegerField()