from rest_framework.routers import DefaultRouter
from core import viewsets

router = DefaultRouter()
router.register('state', viewsets.StateViewSet)
router.register('city', viewsets.CityViewSet)
router.register('zone', viewsets.ZoneViewSet)
router.register('district', viewsets.DistrictViewSet)
router.register('marital_status', viewsets.MaritalStatusViewSet)
router.register('customer', viewsets.CustomerViewSet)
router.register('branch', viewsets.BranchViewSet)
router.register('department', viewsets.DepartmentViewSet)
router.register('employee', viewsets.EmployeeViewSet)
router.register('sale', viewsets.SaleViewSet)
router.register('sale_item', viewsets.SaleItemViewSet)
router.register('supplier', viewsets.SupplierViewSet)
router.register('product_group', viewsets.ProductGroupViewSet)
router.register('product', viewsets.ProductViewSet)

urlpatterns = router.urls
