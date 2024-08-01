from django import forms
from .models import cajaKpi,tradeKpi,stockKpi,expertasKpi

class cajaKpiForm(forms.ModelForm):
    class Meta:
        model = cajaKpi
        fields = ['farmacia', 'legajo', 'tarea', 'fecha', 'cantidad', 'gestionado']
        widgets = {
            'farmacia': forms.Select(attrs={'class': 'form-control'}),
            'legajo': forms.NumberInput(attrs={'class': 'form-control'}),
            'tarea': forms.Select(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'gestionado': forms.Select(attrs={'class': 'form-control'}),
        }


class tradeKpiForm(forms.ModelForm):
    class Meta:
        model = tradeKpi
        fields = ['farmacia', 'legajo', 'tarea', 'fecha', 'cantidad', 'gestionado']
        widgets = {
            'farmacia': forms.Select(attrs={'class': 'form-control'}),
            'legajo': forms.NumberInput(attrs={'class': 'form-control'}),
            'tarea': forms.Select(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'gestionado': forms.Select(attrs={'class': 'form-control'}),
        }


class stockKpiForm(forms.ModelForm):
    class Meta:
        model = stockKpi
        fields = ['farmacia', 'legajo', 'tarea', 'fecha', 'cantidad', 'gestionado']
        widgets = {
            'farmacia': forms.Select(attrs={'class': 'form-control'}),
            'legajo': forms.NumberInput(attrs={'class': 'form-control'}),
            'tarea': forms.Select(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'gestionado': forms.Select(attrs={'class': 'form-control'}),
        }


class expertasKpiForm(forms.ModelForm):
    class Meta:
        model = expertasKpi
        fields = ['farmacia', 'legajo', 'tarea', 'fecha', 'cantidad', 'gestionado']
        widgets = {
            'farmacia': forms.Select(attrs={'class': 'form-control'}),
            'legajo': forms.NumberInput(attrs={'class': 'form-control'}),
            'tarea': forms.Select(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'gestionado': forms.Select(attrs={'class': 'form-control'}),
        }