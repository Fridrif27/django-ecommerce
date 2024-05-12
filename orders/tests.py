from django.test import TestCase
from orders.models import Order, OrderItem
from users.models import User
from goods.models import Products

class OrderModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        user = User.objects.create(first_name='Alex', last_name='Rock', email='alexrock@gmail.com')
        Order.objects.create(user=user, phone_number='380982223445', requires_delivery=True, payment_on_get=True, is_paid=False, status='In processing')

    def test_order_str(self):
        self.assertTrue(Order.objects.exists())
        order = Order.objects.get(id=1)
        self.assertEqual(str(order), f"Order № {order.pk} | Customer {order.user.first_name} {order.user.last_name}")

class OrderItemModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        user = User.objects.create(first_name='Alex', last_name='Rock', email='alexrock@gmail.com')
        product = Products.objects.create(name='Test Product', price=50.00)
        order = Order.objects.create(user=user, phone_number='1234567890', requires_delivery=True, payment_on_get=True, is_paid=False, status='In processing')
        OrderItem.objects.create(order=order, product=product, name='Test Product', price=10.00, quantity=2)

    def test_order_str(self):
        self.assertTrue(Order.objects.exists())
        order = Order.objects.get(id=1)
        self.assertEqual(str(order), f"Order № {order.pk} | Customer {order.user.first_name} {order.user.last_name}")
