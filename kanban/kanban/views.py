from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, "kanban/index.html")
    #render(request, template_name, context) contextは省略されている

@login_required#ログインしてるか確認するデコレーター
def home(request):
    return render(request, "kanban/home.html")

def signup(request):
    if request.method == 'POST': #httpメソッドチェック
        form = UserCreationForm(request.POST)
        if form.is_valid(): #バリデーション
            user_instance = form.save() #データベースに登録
            login(request, user_instance)
            return redirect("kanban:home") #テンプレートの {% url 'kanban:index' %} のリダイレクト版
    else:
        form = UserCreationForm()
        #UserCreationFormとは、
        #HTMLフォームを生成、バリデーション（検証）、入力データの処理などが再利用しやすく簡潔に実装できる

    context = {
        "form": form #elseではなく、ifの方のform
    }
    return render(request, 'kanban/signup.html', context)
