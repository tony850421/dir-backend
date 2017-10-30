"""tutorial2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include

urlpatterns = [
    url(r'^api/', include('snippets.urls')),
    url(r'^api/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^api-token-auth/', 'rest_framework.authtoken.views.obtain_auth_token'),
    # url(r'^api/login/', include('rest_social_auth.urls_session')),
    url(r'^api/tracking/', include('tracking.urls')),
]