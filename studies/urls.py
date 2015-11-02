from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^student/(?P<id_student>\w+)/(?P<id_offer_year>\w+)/(?P<year>\w+)', views.student, name='student'),
    url(r'^attestations/', views.attestations, name='attestations'),
]
