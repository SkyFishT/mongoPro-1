from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$', views.index, name='index'),
    url(r'^manage$', views.manage, name='manage'),
    url(r'^about$', views.show, name='show'),
    url(r'^signin$', views.sign, name='sign'),
    url(r'^signin/action$', views.login_action, name='login_action'),
    url(r'^query/action$', views.query_action, name='query_action'),
    url(r'^edit/(?P<index>\d+)$', views.edit, name='edit_page'),
    url(r'^edit/action$', views.edit_action, name='edit_action'),
    url(r'^delete/(?P<index>\d+)$', views.delete, name='delete'),
]