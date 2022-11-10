from flask import Flask, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

artigos = [
    {
        'id': '0',
        'titulo': 'Titulo 1',
        'conteudo': ['Textao 1', 'imagem']
    },
    {
        'id': 1,
        'titulo': 'Titulo 2',
        'conteudo': ['Textao 2', 'imagem']
    }
]

# retorna um artigo pelo ID, altera artigos e deleta artigos
class Artigo(Resource):
    def get(self, id):
        try:
            response = artigos[id]
        except IndexError:
            mensagem = 'Artigo de ID {} não existe'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido, contate o Administrador da API'
            response = {'status': 'erro', 'mensagem':mensagem}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        artigos[id] = dados
        return dados

    def delete(self, id):
        artigos.pop(id)
        return {'status': 'sucesso', 'mensagem': 'Artigo excluído'}

# Lista todos os artigos e permite registrar novos
class ListaArtigos(Resource):
    def get(self):
        return artigos

    def post(self):
        dados = json.loads(request.data)
        posicao = len(artigos)
        dados['id'] = posicao
        artigos.append(dados)
        return artigos[posicao]

api.add_resource(Artigo, '/artigos/<int:id>/')
api.add_resource(ListaArtigos, '/artigos/')

if __name__ == '__main__':
    app.run(debug=True)