from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from .models import Categoria, Subcategoria, Marca, UnidadMedida
from .form import CategoriaForm, SubCategoriaForm, MarcaForm

####!#  CATEGORIA ###########


class CategoriaView(LoginRequiredMixin, generic.ListView):
    model = Categoria
    template_name = 'inventario/categoria_list.html'
    context_object_name = "obj"
    login_url = "principal:login"


class CategoriaNew(LoginRequiredMixin, generic.CreateView):
    model = Categoria
    template_name = 'inventario/categoria_form.html'
    context_object_name = 'obj'
    form_class = CategoriaForm
    success_url = reverse_lazy("inventario:categoria")
    login_url = "principal:login"

    def form_valid(self, form):
        form.instance.usuario_creado = self.request.user
        return super().form_valid(form)


class CategoriaEdit(LoginRequiredMixin, generic.UpdateView):
    model = Categoria
    template_name = 'inventario/categoria_form.html'
    context_object_name = 'obj'
    form_class = CategoriaForm
    success_url = reverse_lazy("inventario:categoria")
    login_url = "principal:login"

    def form_valid(self, form):
        form.instance.usuario_modificado = self.request.user.id
        return super().form_valid(form)


class CategoriaDel(LoginRequiredMixin, generic.DeleteView):
    model = Categoria
    template_name = 'inventario/catalogos_del.html'
    context_object_name = "obj"
    success_url = reverse_lazy('inventario:categoria')


###! SUBCATEGORIA ###


class SubCategoriaView(LoginRequiredMixin, generic.ListView):
    model = Subcategoria
    template_name = 'inventario/subcategoria_list.html'
    context_object_name = "obj"
    login_url = "principal:login"


class SubCategoriaNew(LoginRequiredMixin, generic.CreateView):
    model = Subcategoria
    template_name = 'inventario/subcategoria_form.html'
    context_object_name = 'obj'
    form_class = SubCategoriaForm
    success_url = reverse_lazy("inventario:subcategoria")
    login_url = "principal:login"

    def form_valid(self, form):
        form.instance.usuario_creado = self.request.user
        return super().form_valid(form)


class SubCategoriaEdit(LoginRequiredMixin, generic.UpdateView):
    model = Subcategoria
    template_name = 'inventario/subcategoria_form.html'
    context_object_name = 'obj'
    form_class = SubCategoriaForm
    success_url = reverse_lazy("inventario:subcategoria")
    login_url = "principal:login"

    def form_valid(self, form):
        form.instance.usuario_modificado = self.request.user.id
        return super().form_valid(form)


class SubCategoriaDel(LoginRequiredMixin, generic.DeleteView):
    model = Subcategoria
    template_name = 'inventario/catalogos_del.html'
    context_object_name = "obj"
    success_url = reverse_lazy('inventario:subcategoria')


#!### MARCA ######


class MarcaView(LoginRequiredMixin, generic.ListView):
    model = Marca
    template_name = 'inventario/marca_list.html'
    context_object_name = "obj"
    login_url = "principal:login"


class MarcaNew(LoginRequiredMixin, generic.CreateView):
    model = Marca
    template_name = 'inventario/marca_form.html'
    context_object_name = 'obj'
    form_class = MarcaForm
    success_url = reverse_lazy("inventario:marca")
    login_url = "principal:login"

    def form_valid(self, form):
        form.instance.usuario_creado = self.request.user
        return super().form_valid(form)


class MarcaEdit(LoginRequiredMixin, generic.UpdateView):
    model = Marca
    template_name = 'inventario/marca_form.html'
    context_object_name = 'obj'
    form_class = MarcaForm
    success_url = reverse_lazy("inventario:marca")
    login_url = "principal:login"

    def form_valid(self, form):
        form.instance.usuario_modificado = self.request.user.id
        return super().form_valid(form)


class MarcaDel(LoginRequiredMixin, generic.DeleteView):
    model = Marca
    template_name = 'inventario/catalogos_del.html'
    context_object_name = "obj"
    success_url = reverse_lazy('inventario:marca')


def marca_inactivar(request, id):
    marca = Marca.objects.filter(pk=id).first()
    contexto = {}
    template_name = "inventario/catalogos_del.html"

    if not marca:
        return redirect("inventario:marca")

    if request.method == "GET":
        contexto = {'obj': marca}
    
    if request.method == "POST":
        marca.estado = False
        marca.save()
        return redirect("inventario:marca")

    return render(request, template_name, contexto)


#!### UNIDADES DE MEDIDA ######

class UnidadMedidaView(LoginRequiredMixin, generic.ListView):
    model = UnidadMedida
    template_name = 'inventario/unidad_list.html'
    context_object_name = "obj"
    login_url = "principal:login"

# class MarcaNew(LoginRequiredMixin, generic.CreateView):
#     model = UnidadMedida
#     template_name = 'inventario/unidad_form.html'
#     context_object_name = 'obj'
#     form_class = UnidadForm
#     success_url = reverse_lazy("inventario:unidad")
#     login_url = "principal:login"

#     def form_valid(self, form):
#         form.instance.usuario_creado = self.request.user
#         return super().form_valid(form)