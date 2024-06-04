from django.db import models


class ModelBase(models.Model):
    objects = None
    id = models.BigAutoField(
        primary_key=True,
        db_column='id',
        verbose_name='ID'
    )

    created_at = models.DateTimeField(
        db_column='created_at',
        null=False,
        auto_now_add=True,
        verbose_name='Created at'
    )

    modified_at = models.DateTimeField(
        db_column='modified_at',
        null=False,
        auto_now=True,
        verbose_name='Modified at'
    )

    active = models.BooleanField(
        db_column='active',
        null=False,
        default=True,
        verbose_name='Active'
    )

    class Meta:
        abstract = True
        managed = True


class State(ModelBase):
    name = models.CharField(
        db_column='name',
        null=False,
        unique=True,
        max_length=64,
        verbose_name='Name',
        error_messages={'unique': 'This state name already exists.'}
    )

    abbreviation = models.CharField(
        db_column='abbreviation',
        null=False,
        unique=True,
        max_length=2,
        verbose_name='Abbreviation',
        error_messages={'unique': 'This abbreviation already exists.'}
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'state'
        verbose_name = 'State'


class City(ModelBase):
    name = models.CharField(
        db_column='name',
        null=False,
        unique=True,
        max_length=64,
        verbose_name='Name',
        error_messages={'unique': 'This city name already exists.'}
    )

    state = models.ForeignKey(
        db_column='id_state',
        to='State',
        null=False,
        on_delete=models.DO_NOTHING
    )

    class Meta:
        db_table = 'city'
        verbose_name = 'City'


class Zone(ModelBase):
    name = models.CharField(
        db_column='name',
        null=False,
        unique=True,
        max_length=64,
        verbose_name='Name',
        error_messages={'unique': 'This zone name already exists.'}
    )

    class Meta:
        db_table = 'zone'
        verbose_name = 'Zone'


class District(ModelBase):
    name = models.CharField(
        db_column='name',
        null=False,
        unique=True,
        max_length=64,
        verbose_name='Name',
        error_messages={'unique': 'This district name already exists.'}
    )
    city = models.ForeignKey(
        db_column='id_city',
        to='City',
        null=False,
        on_delete=models.DO_NOTHING
    )

    zone = models.ForeignKey(
        db_column='id_zone',
        to='Zone',
        null=False,
        on_delete=models.DO_NOTHING
    )

    class Meta:
        db_table = 'district'
        verbose_name = 'District'


class MaritalStatus(ModelBase):
    name = models.CharField(
        db_column='name',
        max_length=64,
        null=False,
        unique=True
    )

    class Meta:
        db_table = 'marital_status'
        verbose_name = 'Marital status'


class Customer(ModelBase):
    class Gender(models.TextChoices):
        MALE = ('M', 'Male')
        FEMALE = ('F', 'Female')

    name = models.CharField(
        db_column='name',
        max_length=64,
        null=False,
        verbose_name='Name',
    )
    income = models.DecimalField(
        db_column='income',
        max_digits=16,
        decimal_places=2,
        null=False,
        verbose_name='Income',
    )
    gender = models.CharField(
        db_column='gender',
        max_length=1,
        choices=Gender.choices,
        null=False,
        verbose_name='Gender'
    )
    district = models.ForeignKey(
        to='District',
        on_delete=models.DO_NOTHING,
        db_column='id_district',
        null=False
    )
    marital_status = models.ForeignKey(
        to='MaritalStatus',
        on_delete=models.DO_NOTHING,
        db_column='id_marital_status',
        null=False
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'customer'
        verbose_name = 'Customer'


class Branch(ModelBase):
    name = models.CharField(
        db_column='name',
        max_length=64,
        null=False,
        verbose_name='Name',
    )
    district = models.ForeignKey(
        to='District',
        on_delete=models.DO_NOTHING,
        db_column='id_district',
        null=False
    )

    class Meta:
        db_table = 'branch'
        verbose_name = 'Branch'


class Department(ModelBase):
    name = models.CharField(
        db_column='name',
        max_length=64,
        null=False,
        verbose_name='Name',
    )

    class Meta:
        db_table = 'department'
        verbose_name = 'Department'


class Employee(ModelBase):
    class Gender(models.TextChoices):
        MALE = ('M', 'Male')
        FEMALE = ('F', 'Female')

    name = models.CharField(
        db_column='name',
        max_length=64,
        null=False,
        verbose_name='Name',
    )
    salary = models.DecimalField(
        db_column='salary',
        max_digits=16,
        decimal_places=2,
        null=False,
        verbose_name='Salary',
    )
    gender = models.CharField(
        db_column='gender',
        max_length=1,
        null=False,
        choices=Gender.choices
    )
    admission_date = models.DateField(
        db_column='admission_date',
        null=False,
        verbose_name='Admission date',
    )
    birth_date = models.DateField(
        db_column='birth_date',
        null=False,
        verbose_name='Birth date',
    )
    district = models.ForeignKey(
        to='District',
        on_delete=models.DO_NOTHING,
        db_column='id_district',
        null=False,
        verbose_name='District',
    )
    department = models.ForeignKey(
        to='Department',
        on_delete=models.DO_NOTHING,
        db_column='id_department',
        null=False,
        verbose_name='Department',
        related_name='employees'
    )
    marital_status = models.ForeignKey(
        to='MaritalStatus',
        on_delete=models.DO_NOTHING,
        db_column='id_marital_status',
        null=False,
        verbose_name='Marital status',
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'employee'
        verbose_name = 'Employee'


class Sale(ModelBase):
    date = models.DateField(
        db_column='date',
        null=False,
        auto_now_add=True,
        verbose_name='Date'
    )

    branch = models.ForeignKey(
        to='Branch',
        on_delete=models.DO_NOTHING,
        db_column='id_branch',
        null=False,
        verbose_name='Branch',
    )

    customer = models.ForeignKey(
        to='Customer',
        on_delete=models.DO_NOTHING,
        db_column='id_customer',
        null=False,
        verbose_name='Customer',
    )

    employee = models.ForeignKey(
        to='Employee',
        on_delete=models.DO_NOTHING,
        db_column='id_employee',
        null=False,
        verbose_name='Employee',
    )

    class Meta:
        db_table = 'sale'
        verbose_name = 'Sale'


class SaleItem(ModelBase):
    sale = models.ForeignKey(
        to='Sale',
        on_delete=models.DO_NOTHING,
        db_column='id_sale',
        null=False,
        verbose_name='Sale'
    )
    product = models.ForeignKey(
        to='Product',
        on_delete=models.DO_NOTHING,
        db_column='id_product',
        null=False,
        verbose_name='Product'
    )
    quantity = models.DecimalField(
        db_column='quantity',
        max_digits=16,
        decimal_places=3,
        null=False,
        verbose_name='Quantity'
    )
    product_price = models.DecimalField(
        db_column='product_price',
        max_digits=16,
        decimal_places=2,
        null=False,
        default=0,
        verbose_name='Product price'
    )

    class Meta:
        db_table = 'sale_item'
        verbose_name = 'Sale item'


class Supplier(ModelBase):
    name = models.CharField(
        db_column='name',
        max_length=64,
        null=False,
        verbose_name='Name'
    )
    legal_document = models.CharField(
        db_column='legal_document',
        max_length=20,
        null=False,
        unique=True,
        verbose_name='Legal document'
    )

    class Meta:
        db_table = 'supplier'
        verbose_name = 'Supplier'


class ProductGroup(ModelBase):
    name = models.CharField(
        db_column='name',
        max_length=64,
        null=False,
        verbose_name='Name'
    )

    commission_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=False,
        db_column='commission_percentage',
        verbose_name='Commission percentage'
    )

    gain_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        db_column='gain_percentage',
        null=False,
        verbose_name='Gain percentage'
    )

    class Meta:
        db_table = 'product_group'
        verbose_name = 'Product group'


class Product(ModelBase):
    name = models.CharField(
        db_column='name',
        max_length=64,
        null=False,
        verbose_name='Name',
    )
    cost_price = models.DecimalField(
        db_column='cost_price',
        max_digits=16,
        decimal_places=2,
        null=False,
        verbose_name='Cost price',
    )
    sale_price = models.DecimalField(
        db_column='sale_price',
        max_digits=16,
        decimal_places=2,
        null=False,
        verbose_name='Sale price',
    )
    product_group = models.ForeignKey(
        to='ProductGroup',
        on_delete=models.DO_NOTHING,
        db_column='id_product_group',
        verbose_name='Product group',
        null=False
    )
    supplier = models.ForeignKey(
        to='Supplier',
        on_delete=models.DO_NOTHING,
        db_column='id_supplier',
        verbose_name='Supplier',
        null=False
    )
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'product'
        verbose_name = 'Product'