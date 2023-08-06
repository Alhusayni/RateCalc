from django.forms import ModelForm
from FlatRate.models import Calculator
from django import forms

class CalcForm(ModelForm):
    class Meta:
        model = Calculator
        fields = ["Price", "Salary", "Years","DownPay", "IntrestRate", "isSupported"]
        labels ={
            'Price': 'قيمة العقار',
            'Salary': 'الراتب',
            'Years': 'عدد السنوات',
            'DownPay': 'الدفعة الأولى',
            'IntrestRate': 'نسبة الفائدة',
            'isSupported': 'مستحق لدعم وزارة الإسكان',
        }

        widgets = {
            'Price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ادخل قيمة العقار'}),
            'Salary': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ادخل الراتب مع كل البدلات وحسم التقاعد'}),
            'Years': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ادخل عدد سنوات التمويل'}),
            'DownPay': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ادخل مبلغ الدفعة الأولى'}),
            'IntrestRate': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'أدخل نسبة الفائدة رقماً'}),
            'isSupported': forms.Select(attrs={'class': 'form-control'}),

        }