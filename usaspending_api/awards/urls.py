from django.conf.urls import include, url

from usaspending_api.awards import views

award_summary_id_patterns = [
    url(r'^autocomplete/', views.AwardListSummaryAutocomplete.as_view())
]

# map reqest types to viewset method; replace this with a router
award_list = views.AwardListViewSet.as_view(
    {'get': 'list', 'post': 'list'})
award_detail = views.AwardListViewSet.as_view(
    {'get': 'retrieve', 'post': 'retrieve'})
award_summary = views.AwardListSummaryViewSet.as_view({
    'get': 'list', 'post': 'list'})
award_total = views.AwardListAggregateViewSet.as_view({
    'get': 'list', 'post': 'list'})

urlpatterns = [
    url(r'$', award_list, name='award-list'),
    url(r'/(?P<pk>[0-9]+)/$', award_detail, name='award-detail'),
    # url(r'^uri/(?P<uri>\w+)', award),
    # url(r'^fain/(?P<fain>\w+)', award),
    # url(r'^piid/(?P<piid>\w+)', award),
    url(r'^summary/', include(award_summary_id_patterns)),
    url(r'^summary/', award_summary),
    url(r'^total/', award_total)
]
