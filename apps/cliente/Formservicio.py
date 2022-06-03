from django import forms
from apps.cliente.models import Servicio

class ServicioForm(forms.ModelForm):
    class Meta:
        model= Servicio
        
        fields = {
            'descripcion',
            'ClienteId',
            'fecha',
            'color',
        }
        
        labels = {
            'descripcion': 'Ingresar la direccion',
            'ClienteId': 'Ingrese modelo',
            'fecha': 'Ingrese nombre',
            'color': 'Ingrese el telefono',
        }
        
        widgets = {
            'descripcion': forms.TextInput(attrs= {'class': 'form-control'}),
            'ClienteId': forms.Select(attrs= {'class': 'form-control'}),
            'fecha': forms.TextInput(attrs= {'class': 'form-control'}),
            'color': forms.TextInput(attrs= {'class': 'form-control'}),  
        }
