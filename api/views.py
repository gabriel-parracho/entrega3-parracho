from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from api.model.Postagem import Postagem
from api.serializers import PostagemSerializer


class PostagemList(APIView):
    def get(self, request):
        postagem = Postagem.objects.all()
        data = PostagemSerializer(postagem, many=True).data

        return Response(data)

    def post(self, request):
        nome = request.data['nome']
        texto = request.data['texto']
        autor = request.user['usuario']
        likes = request.data['numero likes']
        comentarios = request.data['numero comentarios']
        rts = request.data['numero rts']
        postagem = Postagem(nome= nome,
                            texto= texto,
                            autor= autor,
                            likes= likes,
                            comentarios= comentarios,
                            rts= rts
                            )
        postagem.save()
        data = PostagemSerializer(postagem).data

        return Response(data)
# Create your views here.