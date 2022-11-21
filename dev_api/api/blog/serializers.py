from flask_restplus import fields
from dev_api.api.restplus import api

blog_post = api.model('Blog post', {
    'id': fields.Integer(readOnly=True, description='ID unico de um post no blog'),
    'title': fields.String(required=True, description='Titulo do Artigo'),
    'body': fields.String(required=True, description='Conteudo do Artigo'),
    'pub_date': fields.DateTime,
    'category_id': fields.Integer(attribute='category.id'),
    'category': fields.String(attribute='category.name'),
})

pagination = api.model('A page of results', {
    'page': fields.Integer(description='Número desta página nos resultados'),
    'pages': fields.Integer(description='Número total de páginas de resultados'),
    'per_page': fields.Integer(description='Number of items per page of results'),
    'total': fields.Integer(description='Número total de resultados'),
})

page_of_blog_posts = api.inherit('Page of blog posts', pagination, {
    'items': fields.List(fields.Nested(blog_post))
})

category = api.model('Blog category', {
    'id': fields.Integer(readOnly=True, description='Id unico de uma categoria no blog'),
    'name': fields.String(required=True, description='Nome da categoria'),
})

category_with_posts = api.inherit('Blog category with posts', category, {
    'posts': fields.List(fields.Nested(blog_post))
})
