from flask import Flask, request
from flask_restful import Resource, Api
from models import Artigos, Topicos
import json

app = Flask(__name__)
api = Api(app)

class Artigo(Resource):
    def get(self, titulo):
        artigo = Artigos.query.filter_by(titulo=titulo).first()
        try:
            response = {
                'id': artigo.id,
                'titulo': artigo.titulo,
                'conteudo': artigo.conteudo
            }
        except AttributeError:
            response = {
                'status': 'error',
                'mensagem': 'Artigo não encontrado'
            }
        return response

    def put(self, titulo):
        artigo = Artigos.query.filter_by(titulo=titulo).first()
        dados = request.json
        if 'titulo' in dados:
            artigo.titulo = dados['titulo']
        if 'conteudo' in dados:
            artigo.conteudo = dados['conteudo']
        artigo.save()
        response = {
            'id': artigo.id,
            'titulo': artigo.titulo,
            'conteudo': artigo.conteudo
        }
        return response

    def delete(self, titulo):
        artigo = Artigos.query.filter_by(titulo=titulo).first()
        mensagem = 'Artigo {} excluído com sucesso'.format(artigo.titulo)
        artigo.delete()
        return {'status':'sucesso', 'mensagem': mensagem}

class ListaArtigos(Resource):
    def get(self):
        artigos = Artigos.query.all()
        response = [{'id': i.id, 'titulo': i.titulo, 'conteudo': i.conteudo} for i in artigos]
        return response

    def post(self):
        dados = request.json
        artigo = Artigos(titulo=dados['titulo'], conteudo=dados['conteudo'])
        artigo.save()
        response = {
            'id':artigo.id,
            'titulo':artigo.titulo,
            'conteudo':artigo.conteudo
        }
        return response

class ListaTopicos(Resource):
    def get(self):
        topicos = Topicos.query.all()
        response = [{'id': i.id, 'titulo': i.titulo} for i in topicos]
        return response

    def post(self):
        dados = request.json
        artigo = Artigos.query.filter_by(titulo=dados['artigo']).first()
        topico = Topicos(titulo=dados['titulo'], artigo=artigo)
        topico.save()
        response = {
            'titulo': topico.titulo.artigo,
            'id': topico.id
        }
        return response

api.add_resource(Artigo, '/artigo/<string:titulo>/')
api.add_resource(ListaArtigos, '/artigo/')
api.add_resource(ListaTopicos, '/topicos/')

if __name__ == '__main__':
    app.run(debug=True)