from django.shortcuts import render , redirect
from .models import Board

# Create your views here.

def index(request):
    boards = Board.objects.all()
    context = {'boards' : boards}


    return render(request,'html/index.html',context )

def new(request):
    return render(request,'html/new.html',)

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    print(title,content)
    board =Board(title=title, content=content)
    board.save()
    context = {'title': title,'content': content }
    return render(request,'html/create.html',context)

def detail(request, id):
    # Board 클래스를 사용해서 id 값에 맞는 데이터를 가지고 온다.
    # context 로 넘겨서 detail.html 페이지에서 title 과 content 를
    # 출력해본다.
    board = Board.objects.get(id=id)
    context = {'board': board}
    return render(request, 'html/detail.html', context)

def delete(request,id):
    board = Board.objects.get(id=id)
    board.delete()
    return redirect('/boards/')
def edit(request,id):
    board = Board.objects.get(id=id)
    context = {'board': board}
    return render(request,'html/edit.html',context)

def update(request,id):
    board = Board.objects.get(id=id)
    title = request.POST.get('title')
    content = request.POST.get('content')
    board.title = title
    board.content = content

    print(title,content)
    pass