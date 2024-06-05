from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from core import models, serializers, params_serializers, queries, filters


class StateViewSet(viewsets.ModelViewSet):
    queryset = models.State.objects.all()
    serializer_class = serializers.StateSerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = models.City.objects.select_related('state').all()
    serializer_class = serializers.CitySerializer


class ZoneViewSet(viewsets.ModelViewSet):
    queryset = models.Zone.objects.all()
    serializer_class = serializers.ZoneSerializer

    @action(detail=False, methods=['GET'])
    def get_zone_by_name(self, request, *args, **kwargs):
        param_serializer = params_serializers.ZoneByNameSerializer(data=request.query_params)
        param_serializer.is_valid(raise_exception=True)
        validated_data = param_serializer.validated_data
        zone_name = validated_data.get('name')

        self.queryset = self.get_queryset().filter(name__icontains=zone_name)
        return super(ZoneViewSet, self).list(request, *args, **kwargs)


class DistrictViewSet(viewsets.ModelViewSet):
    queryset = models.District.objects.all()
    serializer_class = serializers.DistrictSerializer


class MaritalStatusViewSet(viewsets.ModelViewSet):
    queryset = models.MaritalStatus.objects.all()
    serializer_class = serializers.MaritalStatusSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer


class BranchViewSet(viewsets.ModelViewSet):
    queryset = models.Branch.objects.all()
    serializer_class = serializers.BranchSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer

    @action(detail=False, methods=['GET'])
    def employee_count_by_department(self, request, *args, **kwargs):
        # Validação dos parâmetros da requisição
        param_serializer = params_serializers \
            .EmployeeCountByDepartmentSerializer(data=request.query_params)

        param_serializer.is_valid(raise_exception=True)
        validated_data = param_serializer.validated_data
        depart_name = validated_data.get('name')

        # Aplicação dos parâmetros validados/serializados
        result = queries.employee_count_by_department(name=depart_name)

        # Validação da query resultante
        # result_serializer = results_serializers.EmployeeCountByDepartmentSerializer(data=result, many=True)
        # result_serializer.is_valid(raise_exception=True)
        # result_data = result_serializer.validated_data

        # Envio do resultado serializado
        return Response(result, status=status.HTTP_200_OK)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
    filter_class = filters.EmployeeFilter
    ordering = ('-id',)
    ordering_fields = '__all__'


class SaleViewSet(viewsets.ModelViewSet):
    queryset = models.Sale.objects.all()
    serializer_class = serializers.SaleSerializer


class SaleItemViewSet(viewsets.ModelViewSet):
    queryset = models.SaleItem.objects.all()
    serializer_class = serializers.SaleItemSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = models.Supplier.objects.all()
    serializer_class = serializers.SupplierSerializer


class ProductGroupViewSet(viewsets.ModelViewSet):
    queryset = models.ProductGroup.objects.all()
    serializer_class = serializers.ProductGroupSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
