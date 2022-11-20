from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from data.passwordinfo_data import passwordinfo,passwordinfo1,passwordinfo2,passwordinfo3,passwordinfo4
from data.user_data import user,user1
# Create your tests here.


class PasswordInfoListsTests(APITestCase):
    def setUp(self):
        self.client.post(reverse("signup"),user,format='json')
        self.client.post(reverse("signup"),user1,format='json')
        usertokens = self.client.post(reverse('token_obtain_pair'),{"username":user['username'],'password':user['password']},format='json')
        header = usertokens.data["access"]
        self.headers = f"Bearer {header}"
        
        usertokens1 = self.client.post(reverse('token_obtain_pair'),{"username":user1['username'],'password':user1['password']},format='json')
        header1 = usertokens1.data["access"]
        
        self.headers1 = f"Bearer {header1}"
        self.client.credentials(HTTP_AUTHORIZATION=self.headers)
        self.client.post(reverse('addpassword'),passwordinfo,format='json')
        self.client.post(reverse('addpassword'),passwordinfo1,format='json')
        self.client.post(reverse('addpassword'),passwordinfo2,format='json')
        self.client.post(reverse('addpassword'),passwordinfo3,format='json')
        self.client.post(reverse('addpassword'),passwordinfo4,format='json')
    
    def test_retrieves_all_passwordinfo_without_authentication(self):
        self.client.credentials()
        response = self.client.get(reverse("passwordlist"))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        # self.assertEqual(response.data,[])
    
    # def test_retrieves_all_passwordinfo_without_authorization(self):
    #     # self.client.credentials()/
    #     self.client.credentials(HTTP_AUTHORIZATION=self.headers1)
    #     response = self.client.get(reverse("passwordlist"))
    #     self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_retrieves_all_passwordinfo(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.headers)
        response = self.client.get(reverse("passwordlist"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.data, [])

  
               
class AddPasswordInfoTests(APITestCase):
    def setUp(self):
        self.client.post(reverse("signup"),user,format='json')
        usertokens = self.client.post(reverse('token_obtain_pair'),{"username":user['username'],'password':user['password']},format='json')
        header = usertokens.data["access"]
        self.headers = f"Bearer {header}"
        self.client.credentials(HTTP_AUTHORIZATION=self.headers)

    def test_create_passwordinfo(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.headers)
        response = self.client.post(reverse("addpassword"),passwordinfo,format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['password'],passwordinfo['password'])
        self.assertEqual(response.data["organization"],passwordinfo['organization'])
        self.assertEqual(response.data['username'],passwordinfo['username'])
           
    def test_create_passwordinfo_without_authentication(self):
        self.client.credentials()
        response = self.client.post(reverse("addpassword"),passwordinfo,format='json')  
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)

class RetrievePasswordInfoTests(APITestCase):
    def setUp(self):
        self.client.post(reverse('signup'),user,format='json')
        self.client.post(reverse('signup'),user1,format='json')
        usertokens = self.client.post(reverse('token_obtain_pair'),{"username":user['username'],'password':user['password']},format='json')
        header = usertokens.data["access"]
        self.headers = f"Bearer {header}"
        usertokens1 = self.client.post(reverse('token_obtain_pair'),{"username":user1['username'],'password':user1['password']},format='json')
        header1 = usertokens1.data["access"]
        self.headers1 = f"Bearer {header1}"
        self.client.credentials(HTTP_AUTHORIZATION=self.headers)
        self.client.post(reverse('addpassword'),passwordinfo,format='json') 
        self.client.post(reverse('addpassword'),passwordinfo1,format='json')
        self.client.post(reverse('addpassword'),passwordinfo2,format='json')
        self.client.post(reverse('addpassword'),passwordinfo3,format='json')

    def test_retrieve_passwordinfo_with_authentication_authorization(self):
        response = self.client.get(reverse('retrievepassword',kwargs={'pk':2}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['password'],passwordinfo1['password'])
        self.assertEqual(response.data["organization"],passwordinfo1['organization'])
        self.assertEqual(response.data['username'],passwordinfo1['username'])
        
    def test_retrieve_passwordinfo_without_authentication(self):
        self.client.credentials()
        response = self.client.get(reverse('retrievepassword',kwargs={'pk':2}))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_retrieve_passwordinfo_without_authorization(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.headers1)
        response = self.client.get(reverse('retrievepassword',kwargs={'pk':2}))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_retrieve_passwordinfo_404(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.headers)
        response = self.client.get(reverse('retrievepassword',kwargs={'pk':45}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
class UpdatePasswordInfoTests(APITestCase):
    def setUp(self):
        self.client.post(reverse("signup"),user,format='json')
        self.client.post(reverse("signup"),user1,format='json')
        usertokens = self.client.post(reverse('token_obtain_pair'),{"username":user['username'],'password':user['password']},format='json')
        header = usertokens.data["access"]
        self.headers = f"Bearer {header}"
        usertokens1 = self.client.post(reverse('token_obtain_pair'),{"username":user1['username'],'password':user1['password']},format='json')
        header1 = usertokens1.data["access"]
        self.headers1 = f"Bearer {header1}"
        self.client.credentials(HTTP_AUTHORIZATION=self.headers)
        self.client.post(reverse('addpassword'),passwordinfo,format='json')
        self.updated_data = passwordinfo3

    def test_update_passwordinfo_with_authentication_and_authorization(self):
        response = self.client.put(reverse("editpassword",kwargs={'pk':1}),self.updated_data,format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_update_passwordinfo_without_authentication(self):
        self.client.credentials()
        response = self.client.put(reverse("editpassword",kwargs={'pk':1}),self.updated_data,format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_update_passwordinfo_without_authorization(self):
        self.client.credentials()
        self.client.credentials(HTTP_AUTHORIZATION=self.headers1)
        response = self.client.put(reverse("editpassword",kwargs={'pk':1}),self.updated_data,format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
    
    def test_update_passwordinfo_404(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.headers)
        response = self.client.put(reverse("editpassword",kwargs={'pk':6}),self.updated_data,format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class DeletePasswordInfoTests(APITestCase):
    def setUp(self):
        self.client.post(reverse("signup"),user,format='json')
        self.client.post(reverse("signup"),user1,format='json')
        usertokens = self.client.post(reverse('token_obtain_pair'),{"username":user['username'],'password':user['password']},format='json')
        header = usertokens.data["access"]
        self.headers = f"Bearer {header}"
        usertokens1 = self.client.post(reverse('token_obtain_pair'),{"username":user1['username'],'password':user1['password']},format='json')
        header1 = usertokens1.data["access"]
        self.headers1 = f"Bearer {header1}"
        self.client.credentials(HTTP_AUTHORIZATION=self.headers)
        self.client.post(reverse('addpassword'),passwordinfo,format='json') 
        self.client.post(reverse('addpassword'),passwordinfo1,format='json')
        self.client.post(reverse('addpassword'),passwordinfo2,format='json')
        self.client.post(reverse('addpassword'),passwordinfo3,format='json')
    
    def test_delete_passwordinfo_with_authentication_authorization(self):
        response = self.client.delete(reverse('deletepassword',kwargs={'pk':1}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_delete_passwordinfo_without_authentication(self):
        self.client.credentials()
        response = self.client.delete(reverse('deletepassword',kwargs={'pk':2}))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_delete_passwordinfo_without_authorization(self):
        self.client.credentials()
        self.client.credentials(HTTP_AUTHORIZATION=self.headers1)
        response = self.client.delete(reverse('deletepassword',kwargs={'pk':2}))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    

    def test_delete_passwordinfo_404(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.headers)
        response = self.client.delete(reverse('deletepassword',kwargs={'pk':45}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
