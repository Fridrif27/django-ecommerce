from django.test import TestCase
from django.utils import timezone
from .models import Order, OrderItem
from users.models import User
from goods.models import Products, Categories


class OrderModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user for testing
        cls.user = User.objects.create(
            first_name="John",
            last_name="Doe",
            email="john@example.com"
        )

        # Create categories for testing
        cls.category = Categories.objects.create(
            name="Test Category",
            slug="test-category"
        )

        # Create some products for testing
        cls.product1 = Products.objects.create(
            name="Product 1",
            price=10.00,
            quantity=5,
            category=cls.category
        )
        cls.product2 = Products.objects.create(
            name="Product 2",
            price=15.00,
            quantity=10,
            category=cls.category
        )

        # Create an order for testing
        cls.order = Order.objects.create(
            user=cls.user,
            card_number="1234567890123456",
            payment_on_get=True,
            is_paid=False,
            status="In processing"
        )

        # Create order items for testing
        cls.order_item1 = OrderItem.objects.create(
            order=cls.order,
            product=cls.product1,
            name=cls.product1.name,
            price=cls.product1.sell_price(),  # Use sell_price instead of price
            quantity=2
        )
        cls.order_item2 = OrderItem.objects.create(
            order=cls.order,
            product=cls.product2,
            name=cls.product2.name,
            price=cls.product2.sell_price(),  # Use sell_price instead of price
            quantity=1
        )

    def test_order_str(self):
        expected_str = f"Order № {self.order.pk} | Customer John Doe"
        self.assertEqual(str(self.order), expected_str)

    def test_order_total_price(self):
        expected_total_price = (self.product1.sell_price() * self.order_item1.quantity) + \
                               (self.product2.sell_price() * self.order_item2.quantity)
        self.assertEqual(self.order.orderitem_set.total_price(), expected_total_price)

    def test_order_total_quantity(self):
        expected_total_quantity = self.order_item1.quantity + self.order_item2.quantity
        self.assertEqual(self.order.orderitem_set.total_quantity(), expected_total_quantity)
