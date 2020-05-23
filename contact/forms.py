from django import forms

class ContactForms(forms.Form):
    name = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={'class':'form-control'}
    ), min_length= 10, max_length= 150)
    email = forms.EmailField(label="Email", required=True, widget=forms.TextInput(
        attrs={'class':'form-control'}
    ), min_length= 10, max_length= 150)
    content = forms.CharField(label="Contenido", required=True, widget=forms.Textarea(
        attrs={'class':'form-control', 'rows':3}
    ))