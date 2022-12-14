import logging.config

import os
from flask import Flask, Blueprint
from dev_api import settings
from dev_api.api.blog.endpoints.posts import ns as blog_posts_namespace
from dev_api.api.blog.endpoints.categories import ns as blog_categories_namespace
from dev_api.api.restplus import api
from dev_api.database import db

app = Flask(__name__, static_url_path='', static_folder='../static')
logging_conf_path = os.path.normpath(os.path.join(os.path.dirname(__file__), '../logging.conf'))
logging.config.fileConfig(logging_conf_path)
log = logging.getLogger(__name__)


def configure_app(flask_app):
    # flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP




def main():
    configure_app(app)
    # log.info('>>>>> Starting development server at http://{}/api/ <<<<<'.format(app.config['SERVER_NAME']))
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(blog_posts_namespace)
    api.add_namespace(blog_categories_namespace)
    app.register_blueprint(blueprint)
    print(app.url_map)
    db.init_app(app)

    app.run(port= os.getenv("PORT", 8081),debug=settings.FLASK_DEBUG, host="0.0.0.0")


