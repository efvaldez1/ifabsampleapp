from wtforms import Form, StringField,IntegerField,DateField,validators
from wtforms.validators import DataRequired
from flask_appbuilder.fieldwidgets import BS3TextFieldWidget
from flask_appbuilder.forms import DynamicForm


class ProfileForm(DynamicForm):
    id = IntegerField(('id'))
    fname = StringField(('fname'),description=('First Name'),validators = [DataRequired()], widget=BS3TextFieldWidget())
    lname = StringField(('lname'),description=('Last Name'), widget=BS3TextFieldWidget())
    email = StringField(('email'),description=('Last Name'), widget=BS3TextFieldWidget())
    birthday=DateField("birthday")
    streetAddress=StringField("streetAddress", [validators.DataRequired()])
    country=StringField("country", [validators.DataRequired()])
    city=StringField("city", [validators.Length(min=4, max=25)])
    state=StringField("state", [validators.Length(min=4, max=25)])
    zipCode=StringField("zipCode", [validators.Length(min=4, max=25)])
    ethereumAddress=StringField("ethereumAddress", [validators.DataRequired()])
    govID=StringField("govID", [validators.Length(min=4, max=25)])