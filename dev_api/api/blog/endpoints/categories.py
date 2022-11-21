import logging

from flask import request
from flask_restplus import Resource
from dev_api.api.blog.business import create_category, delete_category, update_category
from dev_api.api.blog.serializers import category, category_with_posts
from dev_api.api.restplus import api
from dev_api.database.models import Category

log = logging.getLogger(__name__)

ns = api.namespace('blog/categories', description='Classes e métodos responsáveis pelas categorias no blog')


@ns.route('/')
class CategoryCollection(Resource):

    @api.marshal_list_with(category)
    def get(self):
        """
        Retorna lista de categorias no blog
        """
        categories = Category.query.all()
        return categories

    @api.response(201, 'Categoria criada com sucesso.')
    @api.expect(category)
    def post(self):
        """
        Cria uma nova categoria
        """
        data = request.json
        create_category(data)
        return None, 201


@ns.route('/<int:id>')
@api.response(404, 'Categoria não encontrada.')
class CategoryItem(Resource):

    @api.marshal_with(category_with_posts)
    def get(self, id):
        """
        Retorna uma categoria com uma lista de artigos
        """
        return Category.query.filter(Category.id == id).one()

    @api.expect(category)
    @api.response(204, 'Categoria atualizada com sucesso.')
    def put(self, id):
        """
        Atualiza uma categoria no blog.

        Use este método para alterar o nome de uma categoria no blog.

        * Mande um objeto JSON com o novo nome no corpo da solicitação.

        ```
        {
          "name": "Novo nome da categoria"
        }
        ```

        * Especifique o ID da categoria que será modificada no caminho da URL da solicitação.
        """
        data = request.json
        update_category(id, data)
        return None, 204

    @api.response(204, 'Categoria deleta com sucesso')
    def delete(self, id):
        """
        Deleta uma categoria no blog
        """
        delete_category(id)
        return None, 204
