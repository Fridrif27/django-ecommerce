from django.test import TestCase
from .models import Categories, Products
from decimal import Decimal


class CategoriesModelTestCase(TestCase):
    def setUp(self):
        self.category = Categories.objects.create(name='Electronics', slug='electronics', icon='fa fa-laptop')

    def test_category_creation(self):
        self.assertEqual(self.category.name, 'Electronics')
        self.assertEqual(self.category.slug, 'electronics')
        self.assertEqual(self.category.icon, 'fa fa-laptop')

    def test_category_str_method(self):
        self.assertEqual(str(self.category), 'Electronics')

    def test_category_verbose_name_plural(self):
        self.assertEqual(str(Categories._meta.verbose_name_plural), 'Categories')


class ProductsModelTestCase(TestCase):
    def setUp(self):
        category = Categories.objects.create(name='Laptops')
        self.product = Products.objects.create(
            name='Laptop',
            slug='laptop',
            price=1000.00,
            quantity=5,
            description='A powerful laptop',
            category=category
        )

    def test_product_creation(self):
        self.product = Products.objects.get(name='Laptop')
        self.assertEqual(self.product.description, 'A powerful laptop')

    def test_product_display_id(self):
        self.product = Products.objects.get(name='Laptop')
        self.assertEqual(self.product.display_id(), '00001')

    def test_product_get_absolute_url(self):
        self.product = Products.objects.get(name='Laptop')
        self.assertEqual(self.product.get_absolute_url(), '/catalog/product/laptop/')

    def test_product_sell_price_with_discount(self):
        self.product = Products.objects.get(name='Laptop')
        self.product.discount = Decimal('10.00')
        self.product.save()
        self.assertEqual(float(self.product.sell_price()), 900.00)

    def test_product_sell_price_without_discount(self):
        self.product.discount = 0.00
        self.product.save()
        self.assertEqual(float(self.product.sell_price()), 1000.00)

    def test_product_str_method(self):
        self.product = Products.objects.get(name='Laptop')
        self.assertEqual(str(self.product), 'Laptop Quantity - 5')
