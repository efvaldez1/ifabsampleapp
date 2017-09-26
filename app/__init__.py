import logging
from flask import Flask,render_template,request,redirect,jsonify
from flask_appbuilder import SQLA, AppBuilder
from sqlalchemy import func

from .models import MyUser,CountryStat
#Override IndexView
from app.index import MyIndexView
#Override Security Manager
from .sec import MySecurityManager

#chatterbot
from chatterbot import ChatBot 
from chatterbot.trainers import ChatterBotCorpusTrainer
import requests
"""
 Logging configuration
"""
#english_bot=ChatBot("Gordon Ramsey",storage_adapter='chatterbot.storage.SQLStorageAdapter',database_uri='postgresql://postgres:admin@localhost/intuitionmachine')
#english_bot.set_trainer(ChatterBotCorpusTrainer)
#english_bot.train("chatterbot.corpus.english")

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__)
app.config.from_object('config')
db = SQLA(app)

appbuilder = AppBuilder(app, db.session,indexview=MyIndexView,security_manager_class=MySecurityManager)



#Get Response From Chatterbot
# @app.route("/get/<string:query>")
# def get_raw_response(query):
# 	return str(english_bot.get_response(query))


# @app.route("/addcountry/")
# def add_coutry():
# 	country=request.args.get('country')
# 	print('remote addr')
# 	print(request.remote_addr)
# 	return redirect("http://localhost:8080/myuserinfoeditview/form")
# 	tempcountry=CountryStat.query(country=form.country.data).first()
# 	if(tempcountry): #if country exists, increment count column
# 	 	countrycount.count=+1
# 	 	print(countrycount.count)
# 	else: #if country does not exists yet, add instance to db.
# 	 	newCountry=CountryStat(country=form.country.data,count=1)
# 	 	print(newCountry)
# 	 	db.session.add(newCountry)
# 	 	db.session.commit()

@app.route("/update/<oldCountry>/<countryData>/<id>/<ipaddr>")
def update_user(id,oldCountry,countryData,ipaddr):
	""" Update CountryStats Tables and IP Address Of User"""
	print(id)
	print(oldCountry)
	print(countryData)
	print(ipaddr)
	tempUser=db.session.query(MyUser).filter_by(id=id).first()
	tempCountry=db.session.query(CountryStat).filter_by(country=countryData).first()
	print(tempCountry)
	print("SD")
	#if same IP addr, don't save
	if tempUser.geoIP==ipaddr:
		pass
	else:
		tempUser.geoIP=ipaddr
		url = 'http://freegeoip.net/json/'+ipaddr
		req=requests.get(url)
		reqJSON = req.json()
		geoLoc = reqJSON['country_name']
		tempUser.geoLoc=geoLoc
	# if same country as before, do nothing
	if oldCountry==countryData:
		print("same ",tempUser.country,countryData)
		return str(id) #exit
	else:	
		if oldCountry=='None': #Don't add to DB or subtract
			pass
		else:
			updateCountry=db.session.query(CountryStat).filter_by(country=oldCountry).first()
			if updateCountry:
				updateCountry.count-=1
				print("old")
	if tempCountry: #if country already exists		
		tempCountry.count+=1
		print("+1")
	else:
		print("new")
		newCountry=CountryStat(country=countryData,count=1)
		db.session.add(newCountry)	
	db.session.commit()
	return str(id)
@app.route("/get/countries")
def get_country_count():
		#countries=db.session.query(MyUser).all()
		countryStat=db.session.query(MyUser.country,func.count(MyUser.country)).group_by(MyUser.country).all()
		countries=[]
		count=[]
		for i in countryStat:
			countries.append(i[0])
			count.append(i[1])
		print(countryStat)
		return jsonify({'countries':countries ,'count':count})


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

db.create_all()