from flask import render_template,redirect,flash
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView,BaseView,expose,SimpleFormView,has_access,IndexView
from app import appbuilder, db
#from app import db
from .forms import ProfileForm
from .models import Profile

class ProfileModelView(ModelView):
	datamodel=SQLAInterface(Profile)
	
"""
    Application wide 404 error handler
"""

class ProfileFormView(SimpleFormView):
	form = ProfileForm
	form_title= "Intuition Machine Subscription Profile"
	message = "profile was submitted"

	def form_get(self,form):
		pass
		#placeholders
	def form_post(self,form):
		#process form
		flash(self.message,'Info')
@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', base_template=appbuilder.base_template, appbuilder=appbuilder), 404



db.create_all()
appbuilder.add_view(ProfileModelView,"See Profiles", icon="fa-folder-open-o", category="Profiles", category_icon='fa-envelope')
appbuilder.add_view(ProfileModelView,"Create Profile", icon="fa-folder-open-o",label='My Form View',category="SignUp", category_icon='fa-address-card')