from flask.ext.appbuilder import Model
from flask.ext.appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn
from sqlalchemy import Column, Integer, String, ForeignKey ,Boolean
from sqlalchemy.orm import relationship
"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""
        
class Profile(Model):
	__tablename__ = 'profiles'
	id = Column(Integer,primary_key=True)
	fname = Column(String(50))
	lname = Column(String(50))
	birthday=Column(String(50))
	email=Column(String(255),unique=True)
	streetAddress=Column(String(255))
	country=Column(String(255))
	city=Column(String(255))
	state=Column(String(255))
	zipCode=Column(String(255))
	ethAddress=Column(String(255))
	govID=Column(String(255))
	geoIP=Column(String(255))
	geoLoc=Column(String(255))
	password=Column(String(255))
	#role_id = Column(Integer(), db.ForeignKey('roles.id'))
	is_admin = Column(Boolean(), default=False)