"""mathblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from blog import settings



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^competition/', include('competition.urls')),
    url(r'^dpa/', include('dpa.urls')),
    url(r'^educational_activities/', include('educational_activities.urls')),
    url(r'', include('feed.urls')),
    url(r'^gallery/', include('gallery.urls')),
    url(r'^lessons/', include('lessons.urls')),
    url(r'^zno/', include('zno.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)