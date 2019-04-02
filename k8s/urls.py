#! /usr/bin/env python
# -*- coding: utf-8 -*-


from django.contrib import admin
from django.urls import path,include
from k8s import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path(r'api/nodes',views.nodes),
    path(r'api/pods',views.pods),
    path(r'api/pvs',views.pvs),
    path(r'api/namespace',views.namespace),
#  path(r'^k8s',include(k8s.urls)),
]
