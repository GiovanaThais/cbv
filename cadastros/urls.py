from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static
from .views import ClienteList,ClienteCreate,ClienteUpdate,ClienteDelete
from .views import EnderecoList,EnderecoCreate,EnderecoUpdate,EnderecoDelete

urlpatterns = [
    path('',ClienteList.as_view(),name='cliente_list'),
    path('create/',ClienteCreate.as_view(),name='cliente_create'),
    path('update/<int:pk>/',ClienteUpdate.as_view(),name='cliente_update'),
    path('delete/<int:pk>/',ClienteDelete.as_view(),name='cliente_delete'),

    path('list/',EnderecoList.as_view(), name= 'endereco_list'),
    path('createAddress/',EnderecoCreate.as_view(), name = 'endereco_create'),
    path('updateAddress/<int:pk>/',EnderecoUpdate.as_view(), name = 'endereco_update'),
    path('deleteAddress/<int:pk>/',EnderecoDelete.as_view(), name = 'endereco_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)