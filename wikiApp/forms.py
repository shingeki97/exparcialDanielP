from django import forms
from .models import TemaWiki, ArticuloWiki

class TemaWikiForm(forms.ModelForm):
    class Meta:
        model = TemaWiki
        fields = ['nombre', 'descripcion']

class ArticuloWikiForm(forms.ModelForm):
    class Meta:
        model = ArticuloWiki
        fields = ['titulo', 'temaRelacionado', 'contenido']
