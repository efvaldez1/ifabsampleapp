from flask_appbuilder.security.views import UserDBModelView,UserInfoEditView ,AuthDBView,UserStatsChartView # If AUTH_DB
#from flask_appbuilder.security.views import UserOAuthModelView #IF AUTH_OAUTH
from flask_babel import lazy_gettext
from .forms import MyUserInfoEdit,MyRegisterUserDBForm
from flask import request
from flask_appbuilder.security.registerviews import BaseRegisterUser
from flask_appbuilder.models.group import aggregate_count
class MyUserDBModelView(UserDBModelView):
	show_fieldsets = [(lazy_gettext('User info'),{'fields': ['username', 'active', 'roles', 'login_count', 'birthday','streetAddress','country','city','state','zipCode','ethAddress','govID','geoIP','geoLoc']}),(lazy_gettext('Personal Info'),{'fields': ['first_name', 'last_name', 'email'], 'expanded': True}),(lazy_gettext('Audit Info'),{'fields': ['last_login', 'fail_login_count', 'created_on','created_by', 'changed_on', 'changed_by'], 'expanded': False})]
	add_columns = ['first_name', 'last_name', 'username', 'active', 'email', 'roles', 'password', 'conf_password']
	list_columns = ['first_name', 'last_name', 'username', 'email', 'active', 'roles', 'birthday','streetAddress','country','city','state','zipCode','ethAddress','govID','geoIP','geoLoc']
	edit_columns = ['first_name', 'last_name', 'username', 'active', 'email', 'roles',  'birthday','streetAddress','country','city','state','zipCode','ethAddress','govID','geoIP','geoLoc']
	user_info_title = lazy_gettext("Your user information")
	user_show_fieldsets = [(lazy_gettext('Your Profile'),{'fields': ['username', 'active', 'roles', 'login_count', 'birthday','streetAddress','country','city','state','zipCode','ethAddress','govID','geoIP','geoLoc']}),(lazy_gettext('Personal Info'),{'fields': ['first_name', 'last_name', 'email'], 'expanded': True})]

class MyUserStatsChartView(UserStatsChartView):
	 definitions = [
	 	{ 'lable':'Country',
	 	  'group':'country',
	 	  'series':['country']
	 	},
		{
			'label': 'Login Count',
			'group': 'username',
			'series': ['login_count']
		},
		{
			'label': 'Failed Login Count',
			'group': 'username',
			'series': ['fail_login_count']
		}
	]

class MyUserInfoEditView(UserInfoEditView):
	#user info edit page
	form = MyUserInfoEdit
	form_title= lazy_gettext('Edit Your Profile!!!')
	redirect_url='/'
	message='Your Profile Has Been Updated.'
	#user info page
	#user_info_title = lazy_gettext("Your user information")
class MyAuthDBView(AuthDBView):
	login_template='appbuilder/login.html'
class MyRegisterUserDBView(BaseRegisterUser):
	form = MyRegisterUserDBForm
	redirect_url= '/'
	def form_get(self,form):
		self.add_form_unique_validations(form)
	def form_post(self,form):
		print(request.remote_addr)
		self.add_form_unique_validations(form)
		self.add_registration(username=form.username.data,
											  first_name=form.first_name.data,
											  last_name=form.last_name.data,
											  email=form.email.data,
											  password=form.password.data									  
											  )	
		#Can't Edit add_registration method yet
		# self.add_registration(username=form.username.data,
		# 									  first_name=form.first_name.data,
		# 									  last_name=form.last_name.data,
		# 									  email=form.email.data,
		# 									  password=form.password.data,
		# 									  birthday=form.birthday.data,
		# 									  streetAddress=form.streetAddress.data,
		# 									  zipCode=form.zipCode.data,
		# 									  country=form.country.data,
		# 									  ethAddress=form.ethAddress.data,
		# 									  govID=form.govID.data
		# 									  )