from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import ProtectedError
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework.mixins import DestroyModelMixin
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status
from django.db.models.deletion import ProtectedError



#----UD7.2.d----
#Clase de mixin para pasar los campos de plantilla de Update y Create
class CreateUpdateMixin(SuccessMessageMixin):
    url_borrado = None
    success_url = None
    #fields = '__all__'#campos que se van a mostrar en el formulario, __all__ significa que se van a mostrar todos los campos
    template_name = 'common/base_create_update.html'
    success_message = None
    #----UD7.3.a-----
    # Forma del formulario para crear y actualizar cada vista
    form_class = None

    #----UD7.2.d-----
    # Contexto que se pasa a la plantilla y url de redirección
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['verbose_name'] = self.model._meta.verbose_name #nombre de la clase en singular especificado en la clase Meta del modelo
        context['url_borrado'] = self.url_borrado
        return context
    
    def get_success_url(self):
        return reverse_lazy(self.success_url, kwargs={'pk': self.object.pk})


#----UD7.2.f----
#Clase de mixin para elimnar un projecot y verificar las dependencias
class DeleteMixin(SuccessMessageMixin):
    template_name = 'common/base_confirm_delete.html' # ruta plantilla
    success_url = None #url de redirección
    success_message = None #mensaje de eliminacion exitoso
    error_message = None #mensaje de fallo por dependencias de delete
    mensaje_confirmacion = None #mensaje de eliminacion especificado
    objectoDependiente = None #objeto dependiente para verificar si se puede eliminar

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = self.model._meta.verbose_name # titulo en la plantilla
        context['mensaje_confirmacion'] = self.mensaje_confirmacion # mensaje de eliminacion especificado
        context['cancel_url'] = self.success_url # url en el bonton de cancel
        return context

    def get_success_url(self):
        return self.success_url

    #----UD7.2.f-----
    # Verificamos si el objeto tiene dependencias
    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except ProtectedError:
            messages.error(
                self.request,
                self.error_message
            )
            return HttpResponseRedirect(self.success_url)

#----UD7.2.g----
#Clase de mixin para ordenancion con query_set
class OrderedListMixin:
    def get_queryset(self):
        queryset = super().get_queryset()
        ordering = self.request.GET.get('ordering', 'asc')
        if ordering == 'desc':
            return queryset.order_by('-id')
        return queryset.order_by('id')

#----UD8.3---
# Mixin para requerir que el usuario esté autenticado para acceder a las vistas
class LoginRequiredMixin:
    #Decorador para requerir que el usuario esté autenticado para acceder a las vistas
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

#----UD10.3.b----
# Mixin para borrar un objeto con dependencias protegidas heredando de DestroyModelMixin de rest_framework
class ProtectedDeleteMixin(DestroyModelMixin):
    error_message = "No se puede realizar la operación de borrado porque existen dependencias."

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
            instance.delete()
        except ProtectedError:
            raise ValidationError(self.error_message)
        return Response(status=status.HTTP_204_NO_CONTENT)
