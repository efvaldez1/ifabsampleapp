import logging
from flask import Flask,render_template
from flask_appbuilder import SQLA, AppBuilder
#
#from .forms import UserForm
#from .views import MyIndexView

#Override IndexView and User Registration
from app.index import MyIndexView
from .sec import MySecurityManager
"""
 Logging configuration
"""

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__)
app.config.from_object('config')
db = SQLA(app)
#appbuilder = AppBuilder(app, db.session,indexview=MyIndexView)
appbuilder = AppBuilder(app, db.session,indexview=MyIndexView,security_manager_class=MySecurityManager)

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


from app import views

