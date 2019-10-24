from django.urls import path
from api.views import PostagemList
from api.views import UsuarioList

urlpatterns = [
    path('postagem/', PostagemList.as_view()),
    path('usuario/', UsuarioList.as_view())
]