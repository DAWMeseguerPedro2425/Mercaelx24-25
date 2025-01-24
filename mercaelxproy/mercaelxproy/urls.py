"""
URL configuration for mercaelxproy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from common import views as common_views
from core import views as core_views
from usuarios import views as usuarios_views

#--------UD6.7.b--------
#Importar las vistas de la aplicación directorio_comercios con
#  el nombre comercios_views
from directorio_comercios import views as comercios_views

#--------UD10.3.a--------
#Importar las vistas de la aplicación directorio_comercios.api y core.api
from rest_framework import routers
from core.api import views as core_api_views
from directorio_comercios.api import views as comercios_api_views


router = routers.DefaultRouter() # DefaultRouter crea automáticamente las rutas para las vistas de la API

#--------UD10.3.a--------
#Registrar las vistas de la API REST de las aplicaciones core y directorio_comercios
router.register(r'provincia_list', core_api_views.ProvinciaListViewSet, basename='provincia_list')
router.register(r'provincia_crud', core_api_views.ProvinciaDetailViewSet, basename='provincia_crud')
router.register(r'ciudad_list', core_api_views.CiudadListViewSet, basename='ciudad_list')
router.register(r'ciudad_crud', core_api_views.CiudadDetailViewSet, basename='ciudad_crud')
router.register(r'distrito_list', core_api_views.DistritoListViewSet, basename='distrito_list')
router.register(r'distrito_crud', core_api_views.DistritoDetailViewSet, basename='distrito_crud')
router.register(r'asociacion_list', comercios_api_views.AsociacionListViewSet, basename='asociacion_list')
router.register(r'asociacion_crud', comercios_api_views.AsociacionDetailViewSet, basename='asociacion_crud')
router.register(r'categoria_list', comercios_api_views.CategoriaListViewSet, basename='categoria_list')
router.register(r'categoria_crud', comercios_api_views.CategoriaDetailViewSet, basename='categoria_crud')
router.register(r'subcategoria_list', comercios_api_views.SubcategoriaListViewSet, basename='subcategoria_list')
router.register(r'subcategoria_crud', comercios_api_views.SubcategoriaDetailViewSet, basename='subcategoria_crud')
router.register(r'comercio_list', comercios_api_views.ComercioListViewSet, basename='comercio_list')
router.register(r'comercio_crud', comercios_api_views.ComercioDetailViewSet, basename='comercio_crud')
urlpatterns = [
    #--------UD6.2.e-UD6.7--------
    #URLs de la aplicacines
    path('admin/', admin.site.urls),

    # Common URLs
    path('', common_views.HomeView.as_view(), name='home'),
    path('panel/', common_views.PanelView.as_view(), name='panel'),
    
    # Core URLs
    path('provincia_list/', core_views.ProvinciaListView.as_view(), name='provincia_list'),
    path('provincia_detail/<int:pk>/', core_views.ProvinciaDetailView.as_view(), name='provincia_detail'),
    #----UD7.2.b----
    #URLs de crear, actualizar y eliminar una provincia
    path('provincia_create/', core_views.ProvCreateView.as_view(), name='provincia_create'),
    path('provincia_update/<int:pk>/', core_views.ProvUpdateView.as_view(), name='provincia_update'),
    path('provincia_delete/<int:pk>/', core_views.ProvDeleteView.as_view(), name='provincia_delete'),

    path('ciudad_list/', core_views.CiudadListView.as_view(), name='ciudad_list'),
    path('ciudad_detail/<int:pk>/', core_views.CiudadDetailView.as_view(), name='ciudad_detail'),
    #----UD7.2.b----
    #URLs de crear, actualizar y eliminar una ciudad
    path('ciudad_create/', core_views.CiudadCreateView.as_view(), name='ciudad_create'),
    path('ciudad_update/<int:pk>/', core_views.CiudadUpdateView.as_view(), name='ciudad_update'),
    path('ciudad_delete/<int:pk>/', core_views.CiudadDeleteView.as_view(), name='ciudad_delete'),

    path('distrito_list/', core_views.DistritoListView.as_view(), name='distrito_list'),
    path('distrito_detail/<int:pk>/', core_views.DistritoDetailView.as_view(), name='distrito_detail'),
    #----UD7.2.b----
    #URLs de crear, actualizar y eliminar un distrito
    path('distrito_create/', core_views.DistCreateView.as_view(), name='distrito_create'),
    path('distrito_update/<int:pk>/', core_views.DistUpdateView.as_view(), name='distrito_update'),
    path('distrito_delete/<int:pk>/', core_views.DistDeleteView.as_view(), name='distrito_delete'),

    # Directorio Comercios URLs
    path('asociacion_list/', comercios_views.AsociacionListView.as_view(), name='asociacion_list'),
    path('asociacion_detail/<int:pk>/', comercios_views.AsociacionDetailView.as_view(), name='asociacion_detail'),
    #----UD7.2.b----
    #URLs de crear, actualizar y eliminar una asociación
    path('asociacion_create/', comercios_views.AsoCreateView.as_view(), name='asociacion_create'),
    path('asociacion_update/<int:pk>/', comercios_views.AsopdateView.as_view(), name='asociacion_update'),
    path('asociacion_delete/<int:pk>/', comercios_views.AsoDeleteView.as_view(), name='asociacion_delete'),

    path('categoria_list/', comercios_views.CategoriaListView.as_view(), name='categoria_list'),
    path('categoria_detail/<int:pk>/', comercios_views.CategoriaDetailView.as_view(), name='categoria_detail'),
    #----UD7.2.b----
    #URLs de crear, actualizar y eliminar una categoría
    path('categoria_create/', comercios_views.CategoriaCreateView.as_view(), name='categoria_create'),
    path('categoria_update/<int:pk>/', comercios_views.CategoriaUpdateView.as_view(), name='categoria_update'),
    path('categoria_delete/<int:pk>/', comercios_views.CategoriaDeleteView.as_view(), name='categoria_delete'),

    path('subcategoria_list/', comercios_views.SubCategoriaListView.as_view(), name='subcategoria_list'),
    path('subcategoria_detail/<int:pk>/', comercios_views.SubCategoriaDetailView.as_view(), name='subcategoria_detail'),
    #----UD7.2.b----
    #URLs de crear, actualizar y eliminar una subcategoría
    path('subcategoria_create/', comercios_views.SubcategoriaCreateView.as_view(), name='subcategoria_create'),
    path('subcategoria_update/<int:pk>/', comercios_views.SubcategoriaUpdateView.as_view(), name='subcategoria_update'),
    path('subcategoria_delete/<int:pk>/', comercios_views.SubcategoriaDeleteView.as_view(), name='subcategoria_delete'),

    path('comercio_list/', comercios_views.ComercioListView.as_view(), name='comercio_list'),
    path('comercio_detail/<int:pk>/', comercios_views.ComercioDetailView.as_view(), name='comercio_detail'),
    #----UD7.2.b----
    #URLs de crear, actualizar y eliminar un comercio
    path('comercio_create/', comercios_views.ComercioCreateView.as_view(), name='comercio_create'),
    path('comercio_update/<int:pk>/', comercios_views.ComercioUpdateView.as_view(), name='comercio_update'),
    path('comercio_delete/<int:pk>/', comercios_views.ComercioDeleteView.as_view(), name='comercio_delete'),

    #----UD8.2.a----
    # URLs de usuarios
    path('login/', usuarios_views.CustomLoginView.as_view(), name='login'),
    path('logout/', usuarios_views.CustomLogoutView.as_view(), name='logout'),

    #path('accounts/', include('allauth.urls')),

    #----UD10.4----
    #Incluye las URLs de la API REST
    path('api/', include(router.urls)), # Incluye las rutas de la API REST

    #----UD10.3.d-----
    #URL de la API REST para capitalizar nombres
    path('api/capitalize_names/', core_api_views.CapitalizeNamesView.as_view(), name='capitalize_names'),
]

#-----UD6.2.e-----
#Referenciar imagenes en el proyecto
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)