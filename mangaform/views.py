from django.shortcuts import render, redirect, HttpResponse
from .models import MangaData
from .forms import MangaForm

# Create your views here.
# def submit_manga(request):
#     if request.method == 'POST':
#         form = MangaForm(request.POST)
        
#         if form.is_valid():
#             cleaned_data = form.cleaned_data
            
#             character = cleaned_data['character']
#             manga = cleaned_data['manga']
            
#             # new_entry = MangaForm(
#             #     character = character,
#             #     manga = manga
#             # )
#             # new_entry.save()
            
#             MangaData.objects.create(character=character, manga=manga)
            
#             return redirect('mangaform:success')
        
#         else:
#             return render(request, 'mangaform/addManga.html', {'form': form})
        
#     form = MangaForm()
#     return render(request, 'mangaform/addManga.html', {'form': form})

def submit_manga(request):
    form = MangaForm()
    if request.method == 'POST':
        form = MangaForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            
            character = cleaned_data['character']
            manga = cleaned_data['manga']
            
            new_entry = MangaData(
                character = character,
                manga = manga
            )
            new_entry.save()
            
            # MangaData.objects.create(character=character, manga=manga)
            return redirect('mangaform:success')
            
    context = {"form" : form}
    return render(request, 'mangaform/addManga.html', context)

def success(request):
    return HttpResponse('<h2>Form submission was successful!</h2><p>Your data has been saved to the database.</p>')

def overview(request):
    all = MangaData.objects.all()
    one_piece_query = MangaData.objects.filter(manga='One Piece')
    return render(request, 'mangaform/manga.html', {'all': all, 'op': one_piece_query})