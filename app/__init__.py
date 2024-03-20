from flask import Flask
from flask_restx import Api
import logging
from logging.handlers import RotatingFileHandler
import os
from app.utils.dataLoader import load_csv_data_into_db
from app.utils.tableStatus import get_empty_tables
from app.extensions import db
# Import all models here so SQLAlchemy knows about them
from app.models.card_status import PickedUp
from app.models.card_status import Delivered
from app.models.card_status import DeliveryException
from app.models.card_status import Returned
api = Api()
logger = logging.getLogger(__name__)


def configure_logging(app):
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/zywa_services.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Your app startup')


def create_app(config_object='instance.config.DevConfig'):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_object)

    db.init_app(app)
    api.init_app(app, title='Card Status API', version='1.0', description='A service for checking Creditcard statuses')

    with app.app_context():
        # After models are imported, create tables
        db.create_all()

        # Decide on a strategy to determine if the CSV data needs to be loaded
        # For example, you might check if one of the tables is empty
        empty_tables = get_empty_tables()

        if empty_tables:
            load_csv_data_into_db(empty_tables)
        else:
            logger.debug("All tables have data. Skipping data loading.")

        # Import and register your namespaces with the API after the models and db tables are set up
        from app.resources.card_status_resource import api as card_status_namespace
        api.add_namespace(card_status_namespace, path='/api/v1/card_status')
        configure_logging(app)


    return app