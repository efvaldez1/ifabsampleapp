from flask import render_template,redirect,flash
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView,BaseView,expose,SimpleFormView,has_access,IndexView,ModelView
from flask_appbuilder.charts.views import DirectChartView, DirectByChartView, GroupByChartView
from app import appbuilder, db
from flask_appbuilder.models.group import aggregate_count

from .forms import ProfileForm
from .models import Profile,CountryStat
from .sec_views import UserDBModelView

@appbuilder.app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html', base_template=appbuilder.base_template, appbuilder=appbuilder),404

class CountryStatsModelView(ModelView):
	datamodel = SQLAInterface(CountryStat)

	list_columns = ['id','country', 'count']
class CountryStatsDirectChart(DirectByChartView):
	datamodel = SQLAInterface(CountryStat)
	chart_title = 'Statistics'
	definitions = [
	{
		'label': 'Country Statistics',
		'group': 'country',
		'series': ['count']
	}
	]
# class CountryStatsChartView(GroupByChartView):
#     datamodel = SQLAInterface(CountryStat)
#     chart_title = 'Country Statistics Pie Chart'
#     #label_columns = CountryStatsModelView.label_columns
#     chart_type = 'PieChart'
#     definitions = [
#         {
#             'group': 'country',
#             'series': [(aggregate_count,'count')]
#         }
#     ]
#db.create_all()
appbuilder.add_view(CountryStatsModelView,"List Countries", icon="fa-folder-open-o",label='Country List',category="Statistics")
appbuilder.add_view(CountryStatsDirectChart,"Show Country Chart", icon="fa-folder-open-o",label='Country Statistics',category="Statistics")
# appbuilder.add_view(CountryStatsChartView, "Country Pie Chart", icon="fa-dashboard", category="Statistics",label='Country Pie Chart')
