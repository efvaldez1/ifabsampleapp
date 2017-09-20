#from .forms import UserForm
from flask_appbuilder import IndexView
from flask_appbuilder import expose
class MyIndexView(IndexView):
	route_base=''
	default_view='index'
	index_template='appbuilder/index.html'
	#print(UserForm)
	#print(form)
	@expose('/')
#	#@has_access
	def index(self):
		print("HEY\n\n\n")
		#print (form)
		return self.render_template(self.index_template)

