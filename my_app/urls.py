from django.conf.urls import url 
from . import views 


urlpatterns  = [
     url(r'^$',views.index, name = 'index'),
     url('about',views.about, name = 'about'),
     url('contact',views.contact_view, name = 'contact'),
     url('skillset',views.skill_view, name = 'skillset'),
     url('experience',views.exp_view, name = 'experience')
];