from django.urls import path

from . import views

app_name = "kanban" #アプリ名を指定している
#login,logoutはkanban:homeのようにapp_nameの指定ができない（≒指定しなくていい）

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home, name="home"),#ホーム画面
    path('signup/', views.signup, name='signup'),#サインアップページ
]
#path()という関数があり、route , view , name , kwargs の4つの引数を受け取る
#この場合（一番上のpath）、routeは”空”、viewはindex、nameはindex(URLの名称となる)、kwargsは省略
#nameとkwargsは省略できる
#kwargsとは、追加の引数を辞書としてビューに渡せる、殆ど使わない
