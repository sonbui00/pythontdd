from django.conf.urls import include, url
from django.contrib import admin
from lists.views import home_page

urlpatterns = [
    # Examples:
    # url(r'^$', 'superlists.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', home_page, name='home'),
    url(r'^admin/', include(admin.site.urls)),
]
