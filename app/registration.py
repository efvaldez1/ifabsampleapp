from flask_appbuilder.security.registerviews import BaseRegisterUser
from flask_appbuilder.security.sqla.manager import SecurityManager
from flask_appbuilder import expose
class MyRegisterUserDBView(BaseRegisterUser):
	register_template = 'appbuilder/register.html'
	error_message= lazy_gettext('Not possible to register at the moment. Please try again later.')
	message = lazy_gettext('Registration sent to your email!')
class MySecurityManager(SecurityManager):
               registeruserdbview = MyRegisterUserDBView		
