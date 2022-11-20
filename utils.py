from models import Artigos, Usuarios

# Insere dados na tabela artigos
def insere_artigos():
    artigo = Artigos(titulo='Teste1', conteudo='Textao1')
    print(artigo)
    artigo.save()

# Faz consultas na tabela artigos
def consulta_artigos():
    artigo = Artigos.query.all()
    print(artigo)
    artigo = Artigos.query.filter_by(titulo='Teste2').first()
    print(artigo.conteudo)

#Altera dados na tabela artigos
def altera_artigos():
    artigo = Artigos.query.filter_by(titulo='Teste2').first()
    artigo.titulo = 'Novo Titulo'
    artigo.save()

# Exclui dados na tabela artigos
def exclui_artigos():
    artigo = Artigos.query.filter_by(titulo='Teste2').first()
    artigo.delete()

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

if __name__ == '__main__':
    insere_usuario('Admin', '1234')
    insere_usuario('Dev', '456')
    consulta_todos_usuarios()
    #insere_artigos()
    #altera_artigos()
    #exclui_artigos()
    consulta_artigos()