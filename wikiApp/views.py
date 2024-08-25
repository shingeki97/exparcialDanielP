from django.shortcuts import render, redirect
from .models import TemaWiki, ArticuloWiki
from .forms import TemaWikiForm, ArticuloWikiForm

# Vista Principal
def vista_principal(request):
    temas = TemaWiki.objects.all()
    return render(request, 'vista_principal.html', {'temas': temas})

# Crear Nuevo Tema
def crear_nuevo_tema(request):
    if request.method == 'POST':
        form = TemaWikiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vista_principal')
    else:
        form = TemaWikiForm()
    return render(request, 'crear_nuevo_tema.html', {'form': form})

# Crear Nuevo Artículo
def crear_nuevo_articulo(request):
    if request.method == 'POST':
        form = ArticuloWikiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vista_principal')
    else:
        form = ArticuloWikiForm()
    return render(request, 'crear_nuevo_articulo.html', {'form': form})

# Artículos por Tema
def articulos_por_tema(request, tema_id):
    tema = TemaWiki.objects.get(id=tema_id)
    articulos = ArticuloWiki.objects.filter(temaRelacionado=tema)
    return render(request, 'articulos_por_tema.html', {'tema': tema, 'articulos': articulos})

# Vista del Artículo
def vista_articulo(request, articulo_id):
    articulo = ArticuloWiki.objects.get(id=articulo_id)
    return render(request, 'vista_articulo.html', {'articulo': articulo})

# Búsqueda de Artículos
def vista_busqueda(request):
    query = request.GET.get('q', '')
    articulos = ArticuloWiki.objects.filter(titulo__icontains=query)
    return render(request, 'vista_busqueda.html', {'articulos': articulos})
