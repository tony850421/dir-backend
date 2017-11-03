from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

# API endpoints
urlpatterns = format_suffix_patterns([
    url(r'^$', views.api_root),
    url(r'^profiles/$',
        views.ProfileList.as_view(),
        name='profile-list'),
    url(r'^profiles/(?P<pk>[0-9]+)/$',
        views.ProfileDetail.as_view(),
        name='profile-detail'),
    url(r'^socialnetworks/$',
        views.SocialNetworkList.as_view(),
        name='socialnetwork-list'),
    url(r'^socialnetworks/(?P<pk>[0-9]+)/$',
        views.SocialNetworkDetail.as_view(),
        name='socialnetwork-detail'),
    url(r'^tshirts/$',
        views.TShirtList.as_view(),
        name='tshirt-list'),
    url(r'^tshirts/(?P<pk>[0-9]+)/$',
        views.TShirtDetail.as_view(),
        name='tshirt-detail'),
    url(r'^snippets/$',
        views.SnippetList.as_view(),
        name='snippet-list'),
    url(r'^stocks/$',
        views.StockList.as_view(),
        name='stock-list'),
    url(r'^stocks/(?P<pk>[0-9]+)/$',
        views.StockDetail.as_view(),
        name='stock-detail'),
    url(r'^messages/$',
        views.MessageList.as_view(),
        name='message-list'),
    url(r'^messages/(?P<pk>[0-9]+)/$',
        views.MessageDetail.as_view(),
        name='message-detail'),
    url(r'^snippets/(?P<pk>[0-9]+)/$',
        views.SnippetDetail.as_view(),
        name='snippet-detail'),
    url(r'^users/$',
        views.UserList.as_view(),
        name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$',
        views.UserDetail.as_view(),
        name='user-detail'),

    url(r'^claps/$',
        views.ClapList.as_view(),
        name='clap-list'),
    url(r'^claps/(?P<pk>[0-9]+)/$',
        views.ClapDetail.as_view(),
        name='clap-detail')
])

# Login and logout views for the browsable API
urlpatterns += [
    # url(r'^api-auth/', include('rest_framework.urls',
    #                            namespace='rest_framework')),
    url(r'^api-auth/register', views.create_user),
    url(r'^api-auth/update', views.update_user),
    url(r'^updateprofile', views.update_profile),
    url(r'^clap-profile', views.clap_profile),
    url(r'^qrcode', views.qr_generate),
]