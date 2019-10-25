from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from api.model.Postagem import Postagem
from api.model.Usuario import Usuario
from api.model.Comentario import Comentario
from api.serializers import PostagemSerializer
from api.serializers import UsuarioSerializer
from api.serializers import ComentarioSerializer



class PostagemList(APIView):
    def get(self, request):
        postagem = Postagem.objects.all()
        data = PostagemSerializer(postagem, many=True).data

        return Response(data)

    def post(self, request):
        nome = request.data['nome']
        texto = request.data['texto']
        autor = request.data['usuario']
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

class UsuarioList(APIView):
    def get(self, request):
        usuario = Usuario.objects.all()
        data = UsuarioSerializer(usuario, many=True).data

        return Response(data)
    
    def post(self, request):
        nome = request.data['nome']
        nickname = request.data['nickname']
        seguindo = request.data['seguindo']
        seguidores = request.data['seguidores']
        usuario = Usuario(nome= nome,
                          nickname= nickname,
                          seguindo= seguindo,
                          seguidores= seguidores                            
                          )
        usuario.save()
        data = UsuarioSerializer(usuario).data

        return Response(data)

class ComentarioList(APIView):
    def get(self, request):
        comentario = Comentario.objects.all()
        data = ComentarioSerializer(comentario, many=True).data

        return Response(data)

    def post(self, request):
        autor = request.data['autor']
        texto = request.data['texto']
        likes = request.data['numero likes']
        comentario = Comentario(autor= autor,
                                texto= texto,
                                likes= likes
                                )
        comentario.save()
        data = ComentarioSerializer(comentario).data

        return Response(data)

# Create your views here.