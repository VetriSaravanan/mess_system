from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class AccountTests(TestCase):

    def test_register_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')

    def test_user_registration(self):
        data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'phone_number': '1234567890',
            'password1': 'StrongPassword123!',  # Strong password
            'password2': 'StrongPassword123!',
        }
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, 302)  # Expecting a redirect after successful registration
        self.assertTrue(get_user_model().objects.filter(username='testuser').exists())  # Check if the user is created
        self.assertIn('_auth_user_id', self.client.session)  # Check if the user is logged in

    def test_user_login(self):
        User = get_user_model()
        user = User.objects.create_user(username='testuser', password='StrongPassword123!')  # Create user
        data = {
            'username': 'testuser',
            'password': 'StrongPassword123!',
        }
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, 302)  # Should redirect after login
        self.assertIn('_auth_user_id', self.client.session)  # Check if the user is logged in
