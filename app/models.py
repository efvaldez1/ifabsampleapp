from flask.ext.appbuilder import Model
from flask.ext.appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn
from sqlalchemy import Column, Integer, String, ForeignKey 
from sqlalchemy.orm import relationship
"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""
        
class User(Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer,primary_key=True)
	fname = db.Column(db.String(50))
	lname = db.Column(db.String(50))
	birthday=db.Column(db.String(50))
	email=db.Column(db.String(255),unique=True)
	streetAddress=db.Column(db.String(255))
	country=db.Column(db.String(255))
	city=db.Column(db.String(255))
	state=db.Column(db.String(255))
	zipCode=db.Column(db.String(255))
	ethAddress=db.Column(db.String(255))
	govID=db.Column(db.String(255))
	geoIP=db.Column(db.String(255))
	geoLoc=db.Column(db.String(255))
	password=db.Column(db.String(255))
	role_id = db.Column(db.Integer(), db.ForeignKey('roles.id'))
	is_admin = db.Column(db.Boolean(), default=False)