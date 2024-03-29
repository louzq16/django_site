"""channels_example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from channels_example import view
urlpatterns = [
    url(r'^$', view.hello),
    url(r'^admin/', admin.site.urls),
    # video
    url(r'^camera/test1/',view.video_feed_1)
    url(r'^camera/test2/',view.video_feed_2)
    url(r'^camera/test3/',view.video_feed_3)
    url(r'^camera/test4/',view.video_feed_4)
]
