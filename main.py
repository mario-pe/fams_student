from flask import Flask
from flask_restx import Api

from database import init_db
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'DEBUG',
        'handlers': ['wsgi']
    }
})

def create_app():
    from gstudent.resources.student_resource import ns as student_api
    app = Flask(__name__)
    app.logger.info('start app')
    app.config.from_object("settings")
    api = Api(title="student_api", verison="0.1", description="Student manager")
    app.logger.info('init api')
    api.init_app(app)
    api.add_namespace(student_api)
    app.logger.info('finished init api')
    app.logger.info('init DB')
    db = init_db(app)
    return app, api, db

app, api, db = create_app()

if __name__ == '__main__':
    app.run(debug=True)