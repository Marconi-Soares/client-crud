from .models import Client 
from rest_framework.routers import reverse
from rest_framework.test import APITestCase
from rest_framework import status

# Create your tests here.
class ClientViewTestCase(APITestCase):
    def setUp(self):
        self.url = reverse('clientes-list')
        self.url_detail = reverse('clientes-detail', kwargs={'pk':1})
        info_lista = [
                {'idade':18, 'nome':'Marconi'},
                {'idade':20, 'nome':'Juliano'},
                {'idade':50, 'nome':'Maria'}
            ]
        clients = [Client(**info) for info in info_lista]
        Client.objects.bulk_create(clients)

    def test_create(self):
        data = {
            'nome':'Cliente Criado',
            'idade':25
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_read(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update(self):
        data = {
            'nome': 'Marconi Editado',
            'idade': 300
        }
        response = self.client.put(self.url_detail, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        response = self.client.delete(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

