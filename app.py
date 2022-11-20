from flask import Flask, request
from flask_restful import Resource, Api
from models import Artigos, Topicos, Usuarios
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)

# Users = {
#     'Admin': '123',
#     'Analista': '321'
# }

# @auth.verify_password
# def verificacao(login, senha):
#     print('validar usuario')
#     print(Users.get(login) == senha)
#     if not(login, senha):
#         return False
#     return Users.get(login) == senha

@auth.verify_password
def verificacao(login, senha):
    if not(login, senha):
        return False
    return Usuarios.query.filter_by(login=login, senha=senha).first()

class Artigo(Resource):
    @auth.login_required
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
    @auth.login_required
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
            'titulo': topico.titulo,
            'id': topico.id
        }
        return response

api.add_resource(Artigo, '/artigo/<string:titulo>/')
api.add_resource(ListaArtigos, '/artigo/')
api.add_resource(ListaTopicos, '/topicos/')

if __name__ == '__main__':
    app.run(debug=True)