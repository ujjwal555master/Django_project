from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from django.http import HttpResponseRedirect
from django.urls import reverse

# List all notes
def note_list(request):
    notes = Note.objects.all()
    return render(request, 'notes/note_list.html', {'notes': notes})

# View a single note
def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'notes/note_detail.html', {'note': note})

# Add a new note
def add_note(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        file = request.FILES.get('file')
        note = Note.objects.create(title=title, description=description, file=file, uploaded_by=request.user)
        return redirect('note_list')
    return render(request, 'notes/add_note.html')


# Edit an existing note
def edit_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note.title = request.POST.get('title')
        note.description = request.POST.get('description')
        if request.FILES.get('file'):
            note.file = request.FILES.get('file')
        note.save()
        return redirect('note_detail', pk=note.pk)
    return render(request, 'notes/edit_note.html', {'note': note})


# Delete a note
def delete_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('note_list')
    return render(request, 'notes/delete_note.html', {'note': note})
