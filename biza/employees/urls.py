from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^dashboard/$', login_required(TemplateView.as_view(template_name='employees/dashboard.html')), name='employees_dashboard'),
)
