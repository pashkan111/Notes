from django.shortcuts import render


def main(request):
    return render(request, 'notes/notes.html')
