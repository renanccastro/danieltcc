from models import Artigos

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

if __name__ == '__main__':
    #insere_artigos()
    #altera_artigos()
    exclui_artigos()
    consulta_artigos()