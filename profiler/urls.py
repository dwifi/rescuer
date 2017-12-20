from django.conf.urls import url
from .views import urmembersform, urmemformlist,urmem_gridlist, urmemdetails, urmemformdelete, urmemform_update
from .views import urteamform, urteam_list, urteam_details, urteam_delete, urteam_update
from .views import urbloodform, urbloodlist, urblood_details
from .views import uraccidentform, uraccidentlist, uraccident_details, uraccident_delete, uraccident_update




from . import views

app_name = 'profiler'
urlpatterns = [

    url(r'^$', views.home, name='index'),

    url(r'^membersform/$', urmembersform, name='membersform'),
    url(r'^memform_list/$', urmemformlist, name='memform_list'),
    url(r'^mem_gridlist/$', urmem_gridlist, name='mem_girdlist'),
    url(r'^mem_details/(?P<pk>[0-9]+)/$', urmemdetails, name= 'mem_details'),
    url(r'^memform_delete/(?P<pk>[0-9]+)/delete/$', urmemformdelete, name='memform_delete'),
    url(r'^memform_update/(?P<pk>[0-9]+)/update/$', urmemform_update, name='memform_update'),


    url(r'^team_form/$', urteamform, name='team_form'),
    url(r'^team_list/$', urteam_list, name='team_list'),
    url(r'^team_details/(?P<pk>[0-9]+)/$', urteam_details, name='team_details'),
    url(r'^team_delete/(?P<pk>[0-9]+)/delete/$', urteam_delete, name='team_delete'),
    url(r'^team_update/(?P<pk>[0-9]+)/update/$', urteam_update, name='team_update'),


    url(r'^blood_form/$', urbloodform, name='blood_form'),
    url(r'^blood_list/$', urbloodlist, name='blood_list'),
    url(r'^blood_details/(?P<pk>[0-9]+)/$', urblood_details, name='blood_details'),

    url(r'^accident_form/$', uraccidentform, name='accident_form'),
    url(r'^accident_list/$', uraccidentlist, name='accident_list'),
    url(r'^accident_details/(?P<pk>[0-9]+)/$', uraccident_details, name='accident_details'),
    url(r'^accident_delete/(?P<pk>[0-9]+)/delete/$', uraccident_delete, name='accident_delete'),
    url(r'^accident_update/(?P<pk>[0-9]+)/update/$', uraccident_update, name='accident_update'),

]