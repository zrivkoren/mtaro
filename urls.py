from django.conf.urls.defaults import *
from mtaro.contact import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mtaro.views.home', name='home'),
    # url(r'^mtaro/', include('mtaro.foo.urls')),
    url(r'^$', 'mtaro.views.home', name='home'),
    url(r'^mtaro/$', 'mtaro.views.card'),
    url(r'^all/', 'mtaro.views.all', name='all'),
    url(r'^all/$', 'mtaro.views.card'),
    url(r'^random/', 'mtaro.views.random_cards', name='random'),
    url(r'^order/', 'mtaro.views.random_cards_list', name='order'),
    url(r'^contact/', views.contact),
	#url(r'^all/$', current_datetime),
    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
