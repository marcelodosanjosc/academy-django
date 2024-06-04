from rest_framework import serializers


class ZoneByNameSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=256)


class EmployeeCountByDepartmentSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=256)