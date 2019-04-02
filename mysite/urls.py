
from django.contrib import admin
from django.urls import path,include
from cmdb import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path(r'api/nodes',views.nodes),
    path(r'api/node_count',views.node_count),
    path(r'api/pods',views.pods),
    path(r"api/pod_count",views.pod_count),
    path(r'api/pvs',views.pvs),
    path(r'api/pv_count',views.pv_count),
    path(r'api/pvcs',views.pvc),
    path(r'api/pvc_count',views.pvc_count),
    path(r'api/svcs',views.svc),
    path(r'api/svc_count',views.svc_count),
    path(r'api/namespace',views.namespace),
    path(r'api/query',views.query),
    path(r'api/query_count',views.query_count),
    path(r'api/refresh',views.refresh_resource),
]
