import logging
from flask import Flask,render_template
from flask_appbuilder import SQLA, AppBuilder

#Override IndexView
from app.index import MyIndexView
#Override Security Manager
from .sec import MySecurityManager
"""
 Logging configuration
"""

#chatterbot
from chatterbot import ChatBot 
from chatterbot.trainers import ChatterBotCorpusTrainer



english_bot=ChatBot("Gordon Ramsey",storage_adapter='chatterbot.storage.SQLStorageAdapter',database_uri='postgresql://postgres:admin@localhost/intuitionmachine')
english_bot.set_trainer(ChatterBotCorpusTrainer)
english_bot.train("chatterbot.corpus.english")


logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__)
app.config.from_object('config')
db = SQLA(app)
#appbuilder = AppBuilder(app, db.session,indexview=MyIndexView)
appbuilder = AppBuilder(app, db.session,indexview=MyIndexView,security_manager_class=MySecurityManager)


@app.route("/get/<string:query>")
def get_raw_response(query):
    return str(english_bot.get_response(query))
"""
from sqlalchemy.engine import Engine
from sqlalchemy import event

#Only include this for SQLLite constraints
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    # Will force sqllite contraint foreign keys
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()
"""    


from app import models,views

