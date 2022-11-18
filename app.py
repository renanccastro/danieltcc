from flask import Flask, request
from flask_restful import Resource, Api
from models import Artigos
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
#14min
api.add_resource(Artigo, '/artigo/<string:titulo>/')

if __name__ == '__main__':
    app.run(debug=True)