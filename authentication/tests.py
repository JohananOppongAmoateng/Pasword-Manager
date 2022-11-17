from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from data.user_data import user1,user



class TestRegisterUser(APITestCase):
    def test_create_user(self):
        response = self.client.post(reverse('signup'),user,format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['username'],'johanan')
        self.assertEqual(response.data['email'],'ama@gmai.com')
        self.assertEqual(response.data['last_name'],'amoateng')
        self.assertEqual(response.data['first_name'],'johanan')
    
    def test_create_user_bad_request(self):
        response = self.client.post(reverse('signup'),{"username":'johanan',
        'email':'ama@gmai.com',
        'first_name':'johanan',
        'last_name':'amoateng',
        'password':'passwordama',
        },format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        
    
    
class TestMyObtainTokenPairView(APITestCase):
    
    def test_login_user(self):
        self.client.post(reverse('signup'),user,format='json')
       
        response = self.client.post(reverse('token_obtain_pair'),{"username":'johanan','password':'passwordama'},format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)        
        
    def test_login_user_unauthorized(self):
        self.client.post(reverse('signup'),user,format='json')
       
        response = self.client.post(reverse('token_obtain_pair'),{"username":'johanazzsn','password':'passwordamaj'},format='json')
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)  
        
    def test_login_user_bad_request(self):
        self.client.post(reverse('signup'),user,format='json')
        response = self.client.post(reverse('token_obtain_pair'),{"username":'johanan'},format='json')
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)