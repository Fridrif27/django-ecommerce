from django.test import TestCase
from django.urls import reverse
from .models import Categories, Products


class CategoriesModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Categories.objects.create(name='Category1', slug='category1', icon='icon1')

    def test_name_label(self):
        category = Categories.objects.get(id=1)
        field_label = category._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'Name')

    # Add more test methods for other fields and methods


class ProductsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        category = Categories.objects.create(name='Category1', slug='category1', icon='icon1')
        Products.objects.create(name='Product1', slug='product1', description='Description1',
                                 price=100.00, discount=10.00, quantity=10, category=category)

    def test_name_label(self):
        product = Products.objects.get(id=1)
        field_label = product._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'Name')

    # Add more test methods for other fields and methods

    def test_get_absolute_url(self):
        product = Products.objects.get(id=1)
        expected_url = reverse('catalog:product', kwargs={'product_slug': product.slug})
        self.assertEqual(product.get_absolute_url(), expected_url)

    def test_display_id(self):
        product = Products.objects.get(id=1)
        self.assertEqual(product.display_id(), '00001')

    def test_sell_price_with_discount(self):
        product = Products.objects.get(id=1)
        self.assertEqual(product.sell_price(), 90.00)

    def test_sell_price_without_discount(self):
        category = Categories.objects.create(name='Category2', slug='category2', icon='icon2')
        product = Products.objects.create(name='Product2', slug='product2', description='Description2',
                                          price=100.00, quantity=10, category=category)
        self.assertEqual(product.sell_price(), 100.00)

    # Add more test methods for other methods


# Add more test classes for other models if needed
