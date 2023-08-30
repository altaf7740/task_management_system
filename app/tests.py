from django.test import TestCase
from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from .models import Task

class SignupTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.signup_url = reverse('signup')

    def test_valid_signup(self):
        data = {'username': 'king', 'password': 'kingo123'}
        response = self.client.post(self.signup_url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'king')

    def test_invalid_signup_missing_fields(self):
        data = {'username': 'testuser'}
        response = self.client.post(self.signup_url, data, format='json')
        self.assertEqual(response.status_code, 400)

    def test_invalid_signup_existing_user(self):
        User.objects.create_user(username='king', password='kingo123')
        data = {'username': 'king', 'password': 'kingo123'}
        response = self.client.post(self.signup_url, data, format='json')
        self.assertEqual(response.status_code, 400)
    

    def test_invalid_signup_no_password(self):
        data = {'username': 'testuser', 'password': ''}
        response = self.client.post(self.signup_url, data, format='json')
        self.assertEqual(response.status_code, 400)


class TaskViewSetTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token.access_token}')

        self.task_data = {
            'title': 'Test Task',
            'description': 'This is a test task.',
            'status': 'in_progress',
            'due_date': '2023-12-31',
        }
        self.task = Task.objects.create(**self.task_data)


    def test_list_tasks_unauthenticated(self):
        self.client.credentials()  # Clear credentials for unauthenticated request
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_task_authenticated(self):
        response = self.client.post('/api/tasks/', self.task_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_task_unauthenticated(self):
        self.client.credentials()  # Clear credentials for unauthenticated request
        response = self.client.post('/api/tasks/', self.task_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve_task_authenticated(self):
        response = self.client.get(f'/api/tasks/{self.task.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_task_unauthenticated(self):
        self.client.credentials()  # Clear credentials for unauthenticated request
        response = self.client.get(f'/api/tasks/{self.task.id}/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
