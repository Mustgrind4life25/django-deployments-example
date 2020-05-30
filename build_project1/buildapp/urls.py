from django.conf.urls import url
from buildapp import views

# template urls
app_name = 'buildapp'

# Create urls here.

urlpatterns = [
	url(r'^register/$', views.register,name='register'),
	url(r'^user_login/$',views.user_login,name='user_login'),

]