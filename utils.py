from models import Artigos, Usuarios

# Insere dados na tabela artigos
def insere_artigos():
    artigo = Artigos(titulo='Titulo Teste 1', conteudo='Conteudo Teste 1')
    print(artigo)
    artigo.save()

# Faz consultas na tabela artigos
def consulta_artigos():
    artigos = Artigos.query.all()
    print(artigos)
    artigo = Artigos.query.filter_by(titulo='Titulo Teste 2').first()
    print(artigo.conteudo)

# Altera dados na tabela artigos
def altera_artigos():
    artigo = Artigos.query.filter_by(titulo='Titulo Teste 1').first()
    artigo.titulo = 'Novo Titulo Teste 3'
    artigo.save()

# Exclui dados na tabela artigos
def exclui_artigos():
    artigo = Artigos.query.filter_by(titulo='Novo Titulo Teste 3').first()
    artigo.delete()

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

if __name__ == '__main__':
    insere_usuario('AdminTeste', '123')
    insere_usuario('Dev', '456')
    #consulta_todos_usuarios()
    #insere_artigos()
    #altera_artigos()
    #exclui_artigos()
    #consulta_artigos()