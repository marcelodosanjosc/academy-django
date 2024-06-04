from core import models
from django.db.models import Q, Value, FloatField, \
    ExpressionWrapper, F, IntegerField, When, Case, CharField, Count, Sum, Avg, OuterRef, Subquery, Exists
from django.db.models.functions import LPad, Lower, Upper, Cast


def query_all_states():
    all_states = models.State.objects.all()
    print(all_states)


def query_values_employee():
    all_values_employee = models.Zone.objects.values('id', 'name', 'created_at')
    print(all_values_employee)


def query_states_order_by_name():
    all_states = models.State.objects.order_by('name')
    print(all_states)


def query_states_order_by_name_desc():
    all_states = models.State.objects.order_by('-name')
    print(all_states)


def query_customer_order_by_name_and_income():
    all_customers = models.Customer.objects.order_by('name', '-income').values('name', 'income')
    print(all_customers)


def get_employee_ana_luiza():
    result = models.Employee.objects.filter(name='Ana Luiza Cunha')
    print(result)


def get_employee_by_pk():
    result = models.Employee.objects.filter(pk=42)
    print(result)


def get_employee_by_id_42():
    result = models.Employee.objects.filter(id=42)
    print(result)


def get_customer_by_gender():
    result = models.Customer.objects.filter(gender=models.Customer.Gender.MALE)
    print(result)


def get_salary_gt_2000():
    result = models.Employee.objects.filter(salary__gt=2000).order_by('salary').values('name', 'salary')
    print(result)


def get_male_employees_salary_gte_2284():
    result = (models.Employee.objects
              .filter(salary__gte=2284, gender=models.Customer.Gender.MALE)
              .order_by('salary').values('name', 'salary'))
    print(result)


def get_salary_range():
    conditions = Q()
    conditions.add(Q(salary__gte=2000), Q.AND)
    result = models.Employee.objects.filter(conditions).values('name', 'salary')
    print(result)


def get_state_pk_2():
    result = models.State.objects.get(pk=2)
    return result


def get_employee_exception():
    result = models.Employee.objects.get(pk=2)
    return result


def get_employee_by_id(id):
    try:
        result = models.Employee.objects.get(pk=id)
        return result
    except models.Employee.DoesNotExist:
        return 'Employee does not exist'


def get_distinct_suppliers():
    return models.Product.objects.distinct('supplier', 'product_group').values('supplier__name')


def get_total_employees():
    return models.Employee.objects.count()


def get_first_product():
    return models.Product.objects.first()


def get_biggest_customer_income():
    return models.Customer.objects.order_by('-income').first()


def exists_employee_with_some_name(name):
    return models.Employee.objects.filter(name__icontains=name).exists()


def create_department(name):
    return models.Department.objects.create(name=name)


def save_department(name):
    department = models.Department()
    print(f'ANTES DO SAVE: {department.name}')
    department.name = name
    department.save()

    print(f'DEPOIS DO SAVE: {department.name}')


def update_salary_lt_3000():
    return models.Employee.objects.filter(salary__lte=3000).update(salary=4000)


def delete_zone():
    models.Zone.objects.create(name='Centro-Oeste')
    return models.Zone.objects.filter(name__icontains='centro').delete()


def state_dynamic_field_10():
    return models.State.objects.annotate(valor=Value(10)).values('id', 'name', 'valor')


def employee_dynamic_new_salary(increase_tax):
    return (models.Employee.objects.annotate(
        new_salary=ExpressionWrapper((Value(increase_tax) * F('salary')) + F('salary'), output_field=FloatField())
    ).values('name', 'salary', 'new_salary'))


def employee_dynamic_new_salary_2(increase_tax):
    calculo_salario_novo = ExpressionWrapper((Value(increase_tax) * F('salary')) + F('salary'),
                                             output_field=FloatField())

    return (models.Employee.objects.annotate(
        new_salary=calculo_salario_novo
    ).values('name', 'salary', 'new_salary'))


def employee_dynamic():
    return (models.Employee.objects.annotate(
        random_value=ExpressionWrapper(Value(10.5) + Value(30), output_field=IntegerField())
    ).values('name', 'salary', 'random_value'))


def concat_annotate():
    return models.Employee.objects \
        .annotate(new_salary_10=ExpressionWrapper(Value(1.1) * F('salary'), output_field=FloatField())) \
        .annotate(new_salary_20=ExpressionWrapper(Value(1.2) * F('salary'), output_field=FloatField())) \
        .values('name', 'salary', 'new_salary_10', 'new_salary_20')


def join_name():
    return models.Employee.objects \
        .values('name', 'district__name').first()


def changing_join_name():
    return models.Employee.objects \
        .annotate(bairro=F('district__name')) \
        .values('name', 'bairro').first()


def show_gender_verbose_mode():
    return models.Employee.objects.annotate(
        gender_description=Case(
            When(gender=models.Employee.Gender.MALE, then=Value('Masculino')),
            default=Value('Feminino'),
        )
    ).values('name', 'gender', 'gender_description')


def show_rich_people():
    return models.Employee.objects \
        .annotate(
        is_rich=Case(
            When(salary__range=(0, 10000), then=Value('É pobre')),
            When(salary__range=(10000, 20000), then=Value('É rica')),
            default=Value('É muito rico'))) \
        .annotate(eh_rico_ou_pobre_ou_muito_rico=F('is_rich')) \
        .values('name', 'eh_rico_ou_pobre_ou_muito_rico')


def employee_join_department():
    return models.Employee.objects \
               .values('name',
                       'district',
                       'district__name',
                       'district__city__name')[:5]


def filter_employee_by_zone_id(zone_id):
    return models.Employee.objects.filter(district__zone_id=zone_id)


def relacao_inversa():
    return models.Department.objects \
        .filter(pk=14) \
        .filter(employees__salary__gte=10000)


def query_lpad():
    return models.Employee.objects \
        .annotate(id_str=Cast(F('id'), output_field=CharField())) \
        .annotate(code=LPad(expression=F('id_str'), length=7, fill_text=Value('#'))) \
        .values('id', 'code', 'name')


def query_upper_lower():
    return models.Employee.objects \
        .annotate(upper_name=Upper('name')) \
        .annotate(lower_name=Lower('name')) \
        .values('name', 'upper_name', 'lower_name')


def query_count_employee_salary():
    return models.Employee.objects.aggregate(count=Count('id'))


# Group by
def sum_salary_by_gender():
    return models.Employee.objects \
        .values('gender') \
        .annotate(total=Sum('salary'), avg=Avg('salary'))


# Group by
def sum_salary_by_gender_and_marital_status():
    return models.Employee.objects \
        .annotate(estado_civil=F('marital_status__name')) \
        .values('gender', 'estado_civil') \
        .annotate(avg=Avg('salary'))


def last_sale_of_each_product():
    sbq = models.SaleItem.objects.select_related('sale') \
              .filter(product_id=OuterRef('pk')) \
              .values('sale__date') \
              .order_by('-sale__date')[:1]

    return models.Product.objects.annotate(
        last_sale=Subquery(sbq)
    ).values('id', 'last_sale', 'name')


def employee_with_sale():
    sbq = models.Sale.objects.filter(employee_id=OuterRef('id'))
    return models.Employee.objects.annotate(
        has_sale=Exists(sbq)
    ).filter(has_sale=False).values('name', 'has_sale')


def total_sale_of_each_employee():
    sbq = models.SaleItem.objects.select_related('sale') \
              .filter(sale__employee_id=OuterRef('pk')) \
              .annotate(soma=ExpressionWrapper(Sum(F('quantity') * F('product_price')), output_field=FloatField())) \
              .values('soma')[:1]

    return models.Employee.objects.annotate(
        soma=Subquery(sbq)
    ).filter(soma__isnull=False).values('id', 'name', 'soma')


def employee_count_by_department(name):
    return models.Department.objects \
        .filter(name__icontains=name) \
        .values('name') \
        .annotate(qty=Count('employees__id')) \
        .values('name', 'qty')
