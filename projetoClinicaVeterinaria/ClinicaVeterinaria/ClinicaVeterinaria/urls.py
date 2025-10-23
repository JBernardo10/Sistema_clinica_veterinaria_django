"""
URL configuration for ClinicaVeterinaria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.inicio, name="inicio"),
    path('Clinica', views.clinica, name="clinica"),
    path('editarClinica/<int:id>', views.editarClinica, name="editarClinica"),
    path('excluirClinica/<int:id>', views.excluirClinica, name="excluirClinica"),
    path('Cliente', views.cliente, name="cliente"),
    path('editarCliente/<int:id>', views.editarCliente, name="editarCliente"),
    path('excluirCliete/<int:id>', views.excluirCliente, name="excluirCliente"),
    path('Veterinario', views.veterinario, name="veterinario"),
    path('editarVeterinario/<int:id>/', views.editarVeterinario, name='editarVeterinario'),
    path('excluirVeterinario/<int:id>/', views.excluirVeterinario, name='excluirVeterinario'),
    path('pedido/', views.pedido, name="pedido"),
    path('editarPedido/<int:id>', views.editarPedido, name="editarPedido"),
    path('excluirPedido/<int:id>', views.excluirPedido, name="excluirPedido"),
    path('servico/', views.servico, name='servico'),
    path('editarServico/<int:id>/', views.editarServico, name='editarServico'),
    path('excluirServico/<int:id>/', views.excluirServico, name='excluirServico'),
    path('pagamento/', views.pagamento, name='pagamento'),
    path('editarPagamento/<int:id>/', views.editarPagamento, name='editarPagamento'),
    path('excluirPagamento/<int:id>/', views.excluirPagamento, name='excluirPagamento'),
    path('pet/', views.pet, name='pet'),
    path('editarPet/<int:id>/', views.editarPet, name='editarPet'),
    path('excluirPet/<int:id>/', views.excluirPet, name='excluirPet'),
    path('itemServico/', views.itemServico, name='itemServico'),
    path('editarItemServico/<int:id>/', views.editarItemServico, name='editarItemServico'),
    path('excluirItemServico/<int:id>/', views.excluirItemServico, name='excluirItemServico'),
    path('anexo/', views.anexo, name='anexo'),
    path('editarAnexo/<int:id>/', views.editarAnexo, name='editarAnexo'),
    path('excluirAnexo/<int:id>/', views.excluirAnexo, name='excluirAnexo'),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"),name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
