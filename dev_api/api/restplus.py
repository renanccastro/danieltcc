import logging
import traceback

from flask_restplus import Api
from dev_api import settings
from sqlalchemy.orm.exc import NoResultFound

log = logging.getLogger(__name__)

api = Api(version='1.0', title='Blog API',
          description='API para consumo pelo blog frontend')


@api.errorhandler
def default_error_handler(e):
    message = 'Exceção não tratada.'
    log.exception(message)

    if not settings.FLASK_DEBUG:
        return {'message': message}, 500


@api.errorhandler(NoResultFound)
def database_not_found_error_handler(e):
    """Não encontrado nenhum resultado no banco de dados"""
    log.warning(traceback.format_exc())
    return {'message': 'Foi feita uma solicitação ao banco de dados, mas não foram encontrados resultados.'}, 404

