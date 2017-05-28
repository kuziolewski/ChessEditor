from django.shortcuts import render


def index(request):
    return render(request, 'chesseditor/index.html', {})


def edit(request):
    return render(request, 'chesseditor/edit.html', {})


def show(request):
    return render(request, 'chesseditor/show.html', {})


