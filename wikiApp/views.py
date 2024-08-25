from django.shortcuts import render, redirect
from .models import TemaWiki, ArticuloWiki
from .forms import TemaWikiForm, ArticuloWikiForm


def vista_principal(request):
    temas = TemaWiki.objects.all()
    return render(request, 'vista_principal.html', {'temas': temas})


def crear_nuevo_tema(request):
    if request.method == 'POST':
        form = TemaWikiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vista_principal')
    else:
        form = TemaWikiForm()
    return render(request, 'crear_nuevo_tema.html', {'form': form})


def crear_nuevo_articulo(request):
    if request.method == 'POST':
        form = ArticuloWikiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vista_principal')
    else:
        form = ArticuloWikiForm()
    return render(request, 'crear_nuevo_articulo.html', {'form': form})


def articulos_por_tema(request, tema_id):
    tema = TemaWiki.objects.get(id=tema_id)
    articulos = ArticuloWiki.objects.filter(temaRelacionado=tema)
    return render(request, 'articulos_por_tema.html', {'tema': tema, 'articulos': articulos})


def vista_articulo(request, articulo_id):
    articulo = ArticuloWiki.objects.get(id=articulo_id)
    return render(request, 'vista_articulo.html', {'articulo': articulo})


def vista_busqueda(request):
    query = request.GET.get('q', '')
    articulos = ArticuloWiki.objects.filter(titulo__icontains=query)
    return render(request, 'vista_busqueda.html', {'articulos': articulos})
