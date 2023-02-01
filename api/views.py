from rest_framework.viewsets import ModelViewSet 
from .models import Client 
from .serializers import ClientModelSerializer 

# Create your views here.

class ClientViewSet(ModelViewSet):
    serializer_class = ClientModelSerializer 
    queryset = Client.objects.all() 
    
