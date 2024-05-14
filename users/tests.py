from django.contrib.auth import get_user_model
from django.test import TestCase
from users.forms import UserLoginForm

User = get_user_model()

class UserLoginFormTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a user object with valid credentials for testing
        cls.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )

    def test_user_login_form_valid_data(self):
        form = UserLoginForm(data={
            'username': self.user.username,
            'password': 'testpassword'  # Use the correct password
        })
        self.assertTrue(form.is_valid(), form.errors)
