from flask_appbuilder.security.registerviews import BaseRegisterUser
from flask_appbuilder.security.sqla.manager import SecurityManager
from flask_appbuilder import expose
class MyRegisterUserDBView(BaseRegisterUser):
	register_template = 'appbuilder/register.html'
	#@expose('/register/form')
	#def register(self):
	#	print("TEST\n\n\n")
	#	return self.render_template(self.register_template)

class MySecurityManager(SecurityManager):
               registeruserdbview = MyRegisterUserDBView		
