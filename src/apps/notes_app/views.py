from django.shortcuts import render


def main(request):
    return render(request, 'notes/notes.html')


def create_edit(request):
    return render(request, 'notes/create_edit.html')


def edit(request):
    return render(request, 'notes/edit.html')
