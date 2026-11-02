from django.shortcuts import render, redirect, get_object_or_404
from .models import Pokemon, Entrenador, Gimnasio
from .forms import PokemonForm, EntrenadorForm, GimnasioForm 


def lista_pokemones(request):
    pokemones = Pokemon.objects.all().order_by('nombre')[:15]
    entrenadores = Entrenador.objects.all().order_by('nombre')[:10]
    gimnasios = Gimnasio.objects.all()

    context = {
        'pokemones': pokemones,
        'entrenadores': entrenadores,
        'gimnasios': gimnasios,
    }

    return render(request, 'gestion_pokemon/index.html', context)


def crear_pokemon(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES) # request.FILES es crucial para la imagen
        if form.is_valid():
            form.save()
            return redirect('gestion_pokemon:lista_pokemones')
    else:
        form = PokemonForm()
    
    return render(request, 'gestion_pokemon/crear_pokemon.html', {'form': form})

def eliminar_pokemon(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, id=pokemon_id)
    if request.method == 'POST':
        pokemon.delete()
        return redirect('gestion_pokemon:lista_pokemones')
    return render(request, 'gestion_pokemon/eliminar_pokemon.html', {'pokemon': pokemon})

def editar_pokemon(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, id=pokemon_id)
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES, instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect('gestion_pokemon:lista_pokemones')
    else:
        form = PokemonForm(instance=pokemon)
    
    return render(request, 'gestion_pokemon/editar_pokemon.html', {'form': form, 'pokemon': pokemon})

def detalle_pokemon(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, id=pokemon_id)
    return render(request, 'gestion_pokemon/detalle_pokemon.html', {'pokemon': pokemon})


def crear_entrenador(request):
    if request.method == 'POST':
        form = EntrenadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestion_pokemon:lista_pokemones')
    else:
        form = EntrenadorForm()
    return render(request, 'gestion_pokemon/crear_entrenador.html', {'form': form})

def editar_entrenador(request, pk):
    entrenador = get_object_or_404(Entrenador, pk=pk)
    if request.method == 'POST':
        form = EntrenadorForm(request.POST, instance=entrenador)
        if form.is_valid():
            form.save()
            return redirect('gestion_pokemon:lista_pokemones')
    else:
        form = EntrenadorForm(instance=entrenador)
    return render(request, 'gestion_pokemon/editar_entrenador.html', {'form': form, 'entrenador': entrenador})

def eliminar_entrenador(request, pk):
    entrenador = get_object_or_404(Entrenador, pk=pk)
    if request.method == 'POST':
        entrenador.delete()
        return redirect('gestion_pokemon:lista_pokemones')
    return render(request, 'gestion_pokemon/eliminar_entrenador.html', {'entrenador': entrenador})

def detalle_entrenador(request, pk):
    entrenador = get_object_or_404(Entrenador, pk=pk)
    return render(request, 'gestion_pokemon/detalle_entrenador.html', {'entrenador': entrenador})

def crear_gimnasio(request):
    if request.method == 'POST':
        form = GimnasioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestion_pokemon:lista_pokemones')
    else:
        form = GimnasioForm()
    return render(request, 'gestion_pokemon/crear_gimnasio.html', {'form': form})

def detalle_gimnasio(request, pk):
    gimnasio = get_object_or_404(Gimnasio, pk=pk)
    return render(request, 'gestion_pokemon/detalle_gimnasio.html', {'gimnasio': gimnasio})

def editar_gimnasio(request, pk):
    gimnasio = get_object_or_404(Gimnasio, pk=pk)
    if request.method == 'POST':
        form = GimnasioForm(request.POST, instance=gimnasio)
        if form.is_valid():
            form.save()
            return redirect('gestion_pokemon:lista_pokemones')
    else:
        form = GimnasioForm(instance=gimnasio)
    return render(request, 'gestion_pokemon/editar_gimnasio.html', {'form': form, 'gimnasio': gimnasio})

def eliminar_gimnasio(request, pk):
    gimnasio = get_object_or_404(Gimnasio, pk=pk)
    if request.method == 'POST':
        gimnasio.delete()
        return redirect('gestion_pokemon:lista_pokemones')
    return render(request, 'gestion_pokemon/eliminar_gimnasio.html', {'gimnasio': gimnasio})