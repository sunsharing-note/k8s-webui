#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Create your views here.

from django.shortcuts import render,HttpResponse
from k8s import get_nodes,get_pods,get_pv,get_namespace,get_pvc,get_services
from cmdb import models,refresh,get_sourece
import json,os,sys
from django.core import serializers
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


def nodes(request):

    page = request.GET.get("page")
    count = 5
    # all_nodes = get_nodes.get_node()
    nodes = models.UserInfo.objects.all()
    node_count = nodes.count()
    # models.UserInfo.objects.all().delete()
    # if node_count < 1:
    #     for i in all_nodes:
    #         # print("----",i)
    #         name = i["name"]
    #         role = i["role"]
    #         version = i["version"]
    #         status = i["status"]
    #         if status == True:
    #             status = "NoSchedule"
    #         else:
    #             status = "Schedule"
    #         dic = {"name":name,"role":role,"version":version,"status":status}
    #         # print(dic)
    #         models.UserInfo.objects.create(**dic)
    # else:
    #     #pass
    #     #监测是否有node，并尝试去更新status字段
    #     for i in all_nodes:
    #         # print("----",i)
    #         name = i["name"]
    #         role = i["role"]
    #         version = i["version"]
    #         status = i["status"]
    #         if status == True:
    #             status = "NoSchedule"
    #         else:
    #             status = "Schedule"
    #         dic = {"name":name,"role":role,"version":version,"status":status}
    #         flag = models.UserInfo.objects.filter(name=name).exists()
    #         if not flag:
    #             models.UserInfo.objects.create(**dic)
    #         else:
    #             models.UserInfo.objects.filter(name=name).update(status=status)
           
    nodes = models.UserInfo.objects.all()
    page = int(page)
    if page == 1:
        nodes = nodes[0:count]
    elif int(nodes[(page-1)*count:page *count].count()) < count:
        nodes = nodes[(page-1)*count:node_count + 1]
    else:
        nodes = nodes[(page-1)*count:page * count]
        
    # print(nodes)
    nodes = serializers.serialize("json",nodes)
    # return render(request,"user.html",{"data":all_nodes})
    return HttpResponse(nodes)

# node count
def node_count(request):
    count = models.UserInfo.objects.all().count()
    
    return HttpResponse(count)

# pod
def pods(request):
    
    page = request.GET.get("page")
    all_pods = get_pods.get_pods()
    pods = models.pods_info.objects.all()
    pod_count = pods.count()
    # first_id = pods[0]
    # print(page)
    count = 5
    page = int(page)
    # if pod_count < 1:
    #     for i in all_pods:
    #         name = i["name"]
    #         ip = i["pod_ip"]
    #         namespace = i["namespace"]
    #         status = i["status"]
    #         dic = {"name":name,"ip":ip,"namespace":namespace,"status":status}
    #         models.pods_Info.objects.create(**dic)
    # else:
    #     pass
    #     # 尝试去验证每一个pod并尝试更新status
    #     # for i in all_pods:
    #     #     name = i["name"]
    #     #     ip = i["pod_ip"]
    #     #     namespace = i["namespace"]
    #     #     status = i["status"]
    #     #     dic = {"name":name,"ip":ip,"namespace":namespace,"status":status}
    #     #     flag = models.pods_info.objects.filter(name=name).exists()
    #     #     if not flag:
    #     #         models.pods_info.objects.create(**dic)
    #     #     else:
    #     #         models.pods_info.objects.filter(name=name).update(status=status)
    pods = models.pods_info.objects.all()
    if page == 1:
        all_pods = pods[0:count]
        
    # else:
    #     page = int(page)
    #     all_pods = pods[(page-1)*count:page * count]
    elif int(pods[(page-1)*count:page * count].count()) < count:
        all_pods = pods[(page-1)*count:pod_count+1]
    else:
        
        all_pods = pods[(page-1)*count:page * count]

    all_pods = serializers.serialize("json",all_pods)
    return HttpResponse(all_pods)
    # return render(request,"list_pod.html",{"cus_list":customer})

# pod count
def pod_count(request):
    count = models.pods_info.objects.all().count()
    

    return HttpResponse(count)

# pv
def pvs(request):
    page = request.GET.get("page")
    count = 5
    # all_pvs = get_pv.get_pv()
    pvs = models.pvs_info.objects.all()
    pv_count = pvs.count()
    # if pv_count < 1:
    #     for i in all_pvs:
    #         name = i["name"]
    #         capacity = i["capacity"]
    #         access_modes = i["access_modes"]
    #         persistent_volume_reclaim_policy = i["persistent_volume_reclaim_policy"]
    #         status = i["status"]
    #         storage_class_name = i["storage_class_name"]
    #         dic = {"name":name,"capacity":capacity,"access_modes":access_modes,"persistent_volume_reclaim_policy":persistent_volume_reclaim_policy,"status":status,"storage_class_name":storage_class_name}
    #         models.pvs_info.objects.create(**dic)
    # else:
    #     #pass

    #    # 判断是否存在并尝试更新
    #     for i in all_pvs:
    #         name = i["name"]
    #         capacity = i["capacity"]
    #         access_modes = i["access_modes"]
    #         persistent_volume_reclaim_policy = i["persistent_volume_reclaim_policy"]
    #         status = i["status"]
    #         storage_class_name = i["storage_class_name"]
    #         dic = {"name":name,"capacity":capacity,"access_modes":access_modes,"persistent_volume_reclaim_policy":persistent_volume_reclaim_policy,"status":status,"storage_class_name":storage_class_name}
        
    #         flag = models.pvs_info.objects.filter(name=name).exists()
    #         if not flag:
    #             models.pvs_info.objects.create(**dic)
    #         else:
    #             models.pvs_info.objects.filter(name=name).update(status=status)
    page = int(page)
    pvs = models.pvs_info.objects.all()
    if page == 1:
        pvs = pvs[0:count]
    elif int(pvs[(page - 1)*count:page * count].count()) < 5:
        pvs = pvs[(page -1)*count:pv_count + 1]
    else:
        pvs = pvs[(page - 1)*count:page * count]
    return HttpResponse(serializers.serialize("json",pvs))

# pv count
def pv_count(request):
    count = models.pvs_info.objects.all().count()
    

    return HttpResponse(count)
# namespace
def namespace(request):
    # if request.method == "POST":
    all_namespace = get_namespace.get_namespace()
    # print(all_namespace)
    # models.namespace_info.objects.all().delete()
    namespaces = models.namespace_info.objects.all()
    namespace_count = namespaces.count()
    if namespace_count < 1:
        for i in all_namespace:
            name = i["name"]
            dic = {"name":name}
            models.namespace_info.objects.create(**dic)
    else:
        for i in all_namespace:
            name = i["name"]
            dic = {"name":name}
            flag = models.namespace_info.objects.filter(name=name).exists()
            if not flag:
                models.namespace_info.objects.create(**dic)
            else:
                pass
    all_namespace = models.namespace_info.objects.all()
    # all_namespace = get_namespace.get_namespace()
    return HttpResponse(serializers.serialize("json",all_namespace))

def pvc(request):
    page = request.GET.get("page")
    count = 5
    all_pvcs = get_pvc.get_pvc()
    pvcs = models.pvc_info.objects.all()
    pvc_count = pvcs.count()
    # if pvc_count < 1:
    #     for i in all_pvcs:
    #         name = i["name"]
    #         namespace = i["namespace"]
    #         access_mode = i["access_mode"]
    #         capacity = i["capacity"]
    #         phase = i["phase"]
    #         storage_class_name = i["storage_class_name"]
    #         dic = {"name":name,"namespace":namespace,"access_mode":access_mode,"capacity":capacity,"phase":phase,"storage_class_name":storage_class_name}
    #         models.pvc_info.objects.create(**dic)
    # else:
    #     pass
        # for i in all_pvcs:
        #     name = i["name"]
        #     namespace = i["namespace"]
        #     access_mode = i["access_mode"]
        #     capacity = i["capacity"]
        
        #     phase = i["phase"]
        #     storage_class_name = i["storage_class_name"]
        #     dic = {"name": name, "namespace": namespace, "access_mode": access_mode, "capacity": capacity, "phase": phase,
        #            "storage_class_name": storage_class_name}
        
        #     flag = models.pvc_info.objects.filter(name=name).exists()
        #     if not flag:
        #         models.pvc_info.objects.create(**dic)
        #     else:
        #         models.pvc_info.objects.filter(name=name).update(phase=phase)
    page = int(page)
    pvcs = models.pvc_info.objects.all()
    if page == 1:
        pvcs = pvcs[0:count]
    elif int(pvcs[(page - 1)*count:page * count].count()) < 5:
        pvcs = pvcs[(page -1)*count:pvc_count + 1]
    else:
        pvcs = pvcs[(page - 1)*count:page * count]
    return HttpResponse(serializers.serialize("json",pvcs))
def pvc_count(request):
    count = models.pvc_info.objects.all().count()
    return HttpResponse(count)

def svc(request):
    page = request.GET.get("page")
    count = 5
    all_svcs = get_services.get_svc()
    svcs = models.svc_info.objects.all()
    svc_count = svcs.count()
    # if svc_count < 1:
    #     for i in all_svcs:
    #         name = i["name"]
    #         namespace = i["namespace"]
    #         cluster_ip = i["cluster_ip"]
    #         node_port = i["node_port"]
    #         port = i["port"]
    #         dic = {"name":name,"namespace":namespace,"cluster_ip":cluster_ip,"node_port":node_port,"port":port}
    #         models.svc_info.objects.create(**dic)
    # else:
    #     pass
    #     # for i in all_svcs:
    #     #     name = i["name"]
    #     #     namespace = i["namespace"]
    #     #     cluster_ip = i["cluster_ip"]
    #     #     node_port = i["node_port"]
    #     #
    #     #     port = i["port"]
    #     #     dic = {"name":name,"namespace":namespace,"cluster_ip":cluster_ip,"node_port":node_port,"port":port}
    #     #     models.svc_info.objects.create(**dic)
    #     #
    #     #
    #     #
    #     #     flag = models.svc_info.objects.filter(name=name).exists()
    #     #     if not flag:
    #     #         models.svc_info.objects.create(**dic)
    #     #     else:
    #     #         models.svc_info.objects.filter(name=name).update(cluster_ip=cluster_ip)
    page = int(page)
    svcs = models.svc_info.objects.all()
    if page == 1:
        svcs = svcs[0:count]
    elif int(svcs[(page - 1)*count:page * count].count()) < 5:
        svcs = svcs[(page -1)*count:svc_count + 1]
    else:
        svcs = svcs[(page - 1)*count:page * count]
    return HttpResponse(serializers.serialize("json",svcs))
def svc_count(request):
    count = models.svc_info.objects.all().count()
    return HttpResponse(count)
def refresh_resource(request):
    obj = request.GET.get("obj")
    if obj == "node":
        flag = refresh.refresh_nodes()
    elif obj == "pod":
        flag = refresh.refresh_pods()
    elif obj == "pv":
        flag = refresh.refresh_pv()
    elif obj == "service":
        flag = refresh.refresh_svc()
    elif obj == "pvc":
        flag = refresh.refresh_pvc()
    return HttpResponse(flag)

def query(request):
    if request.method == "GET":
        obj = request.GET.get("obj")
        # print(obj)
        namespace = request.GET.get("namespace")
        page = request.GET.get("page")
        try:
            page = int(page)
        except Exception as e:
            page = 1
        count = 5
        # print(namespace)
        if obj == "pvc":
            pvcs = models.pvc_info.objects.filter(namespace=namespace)
            pvcs_count = pvcs.count()
            if pvcs_count < 5:
                objs = pvcs[0:pvcs_count]
            else:
                if page == 1:
                    objs = pvcs[0:count]
                elif int(pvcs[(page - 1)*count:page * count].count()) < 5:
                    objs = pvcs[(page -1)*count:pvcs_count + 1]
                
                else:
                    objs = pvcs[(page - 1)*count:page * count]
        elif obj == "pod":
            pods = models.pods_info.objects.filter(namespace=namespace)
            pods_count = pods.count()
            if pods_count < 5:
                objs = pods[0:pods_count]
            else:
                if page == 1:
                    objs = pods[0:count]
                elif int(pods[(page - 1)*count:page * count].count()) < 5:
                    objs = pods[(page -1)*count:pods_count + 1]
                else:
                    objs = pods[(page - 1)*count:page * count]
        elif obj == "service":
            svcs = models.svc_info.objects.filter(namespace=namespace)
            svcs_count = svcs.count()
            if svcs_count < 5:
                objs = svcs[0:svcs_count]
            else:
                if page == 1:
                    objs = svcs[0:count]
                elif int(svcs[(page - 1)*count:page * count].count()) < 5:
                    objs = svcs[(page -1)*count:svcs_count + 1]
                else:
                    objs = svcs[(page - 1)*count:page * count]

    return HttpResponse(serializers.serialize("json",objs))

def query_count(request):
    if request.method == "GET":
        obj = request.GET.get("obj")
        # print(obj)
        namespace = request.GET.get("namespace")
        if obj == "pvc":
            pvcs = models.pvc_info.objects.filter(namespace=namespace)
            count = pvcs.count()
        elif obj == "pod":
            pods = models.pods_info.objects.filter(namespace=namespace)
            count = pods.count()
        elif obj == "service":
            svcs = models.svc_info.objects.filter(namespace=namespace)
            count = svcs.count()

    return HttpResponse(count)