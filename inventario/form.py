from django import forms
from .models import Categoria,Subcategoria,Marca


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['descripcion', 'estado']
        labels = {
            'descripcion': "Descripcion de la Categoria",
            'estado': "Estado"
        }


        widgets = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {'class': 'form-control'})

class SubCategoriaForm(forms.ModelForm):

    categoria = forms.ModelChoiceField(
        queryset= Categoria.objects.filter(estado = True)
        .order_by('descripcion')
    )

    class Meta:
        model = Subcategoria
        fields = ['categoria','descripcion', 'estado']
        labels = {
            'descripcion': "Sub Categoria",
            'estado': "Estado"
        }


        widgets = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categoria'].empty_label = "Seleccione Categoria"
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {'class': 'form-control'})
        
class MarcaForm(forms.ModelForm):

    class Meta:
        model = Marca
        fields = ['descripcion', 'estado']
        labels = {
            'descripcion': "Descripcion de la Marca",
            'estado': "Estado"
        }

        widgets = {'descripcion': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {'class': 'form-control'})
        