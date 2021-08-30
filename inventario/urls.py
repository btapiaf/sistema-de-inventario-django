from django.urls import path
from .views import CategoriaView, CategoriaNew, CategoriaEdit, CategoriaDel, SubCategoriaEdit, SubCategoriaView, SubCategoriaNew,SubCategoriaDel,MarcaView,MarcaDel, MarcaEdit, MarcaNew, marca_inactivar

urlpatterns = [
    # Categoria
    path("categorias/", CategoriaView.as_view(), name="categoria"),
    path("categorias/nueva", CategoriaNew.as_view(), name="categoria_new"),
    path("categorias/edit/<int:pk>", CategoriaEdit.as_view(), name="categoria_edit"),
    path("categorias/eliminar/<int:pk>", CategoriaDel.as_view(),name="categoria_eliminar"),

    #Subcategoria
    path("subcategorias/", SubCategoriaView.as_view(), name="subcategoria"),
    path("subcategorias/nueva",SubCategoriaNew.as_view(), name="subcategoria_new"),
    path("subcategorias/edit/<int:pk>", SubCategoriaEdit.as_view(), name="subcategoria_edit"),
    path("subcategorias/eliminar/<int:pk>", SubCategoriaDel.as_view(), name="subcategoria_eliminar"),

    #Marca

    path("marca/", MarcaView.as_view(), name="marca"),
    path("marca/nueva",MarcaNew.as_view(), name="marca_new"),
    path("marca/edit/<int:pk>", MarcaEdit.as_view(), name="marca_edit"),
    path("marca/eliminar/<int:id>", marca_inactivar, name="marca_inactivar"),

]