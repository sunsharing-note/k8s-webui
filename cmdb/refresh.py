#! /usr/bin/env python
# -*- coding: utf-8 -*-


from k8s import get_nodes,get_pods,get_pv,get_namespace,get_pvc,get_services
from cmdb import models

def refresh_nodes():
    all_nodes = get_nodes.get_node()
    nodes = models.UserInfo.objects.all()
    node_count = nodes.count()
    # models.UserInfo.objects.all().delete()
    if node_count < 1:
        for i in all_nodes:
            # print("----",i)
            name = i["name"]
            role = i["role"]
            version = i["version"]
            status = i["status"]
            if status == True:
                status = "NoSchedule"
            else:
                status = "Schedule"            
            dic = {"name":name,"role":role,"version":version,"status":status}
            # print(dic)
            models.UserInfo.objects.create(**dic)
    else:
        # pass
        # 监测是否有node，并尝试去更新status字段
        for i in all_nodes:
            # print("----",i)
            name = i["name"]
            role = i["role"]
            version = i["version"]
            status = i["status"]
            if status == True:
                status = "NoSchedule"
            else:
                status = "Schedule"
            dic = {"name":name,"role":role,"version":version,"status":status}
            flag = models.UserInfo.objects.filter(name=name).exists()
            if not flag:
                models.UserInfo.objects.create(**dic)
            else:
                models.UserInfo.objects.filter(name=name).update(status=status)
    return True
def refresh_pods():
    all_pods = get_pods.get_pods()
    pods = models.pods_info.objects.all()
    pod_count = pods.count()
    if pod_count < 1:
        for i in all_pods:
            name = i["name"]
            ip = i["pod_ip"]
            namespace = i["namespace"]
            status = i["status"]
            dic = {"name":name,"ip":ip,"namespace":namespace,"status":status}
            models.pods_Info.objects.create(**dic)
    else:
        # pass
        # 尝试去验证每一个pod并尝试更新status
        for i in all_pods:
            name = i["name"]
            ip = i["pod_ip"]
            namespace = i["namespace"]
            status = i["status"]
            dic = {"name":name,"ip":ip,"namespace":namespace,"status":status}
            flag = models.pods_info.objects.filter(name=name).exists()
            if not flag:
                models.pods_info.objects.create(**dic)
            else:
                models.pods_info.objects.filter(name=name).update(status=status)
    return True
def refresh_pv():
    all_pvs = get_pv.get_pv()
    pvs = models.pvs_info.objects.all()
    pv_count = pvs.count()
    if pv_count < 1:
        for i in all_pvs:
            name = i["name"]
            capacity = i["capacity"]
            access_modes = i["access_modes"]
            persistent_volume_reclaim_policy = i["persistent_volume_reclaim_policy"]
            status = i["status"]
            storage_class_name = i["storage_class_name"]
            dic = {"name":name,"capacity":capacity,"access_modes":access_modes,"persistent_volume_reclaim_policy":persistent_volume_reclaim_policy,"status":status,"storage_class_name":storage_class_name}
            models.pvs_info.objects.create(**dic)
    else:
        # pass

        # 判断是否存在并尝试更新
        for i in all_pvs:
            name = i["name"]
            capacity = i["capacity"]
            access_modes = i["access_modes"]
            persistent_volume_reclaim_policy = i["persistent_volume_reclaim_policy"]
            status = i["status"]
            storage_class_name = i["storage_class_name"]
            dic = {"name":name,"capacity":capacity,"access_modes":access_modes,"persistent_volume_reclaim_policy":persistent_volume_reclaim_policy,"status":status,"storage_class_name":storage_class_name}
        
            flag = models.pvs_info.objects.filter(name=name).exists()
            if not flag:
                models.pvs_info.objects.create(**dic)
            else:
                models.pvs_info.objects.filter(name=name).update(status=status)
    return True
def refresh_pvc():
    all_pvcs = get_pvc.get_pvc()
    pvcs = models.pvc_info.objects.all()
    pvc_count = pvcs.count()
    if pvc_count < 1:
        for i in all_pvcs:
            name = i["name"]
            namespace = i["namespace"]
            access_mode = i["access_mode"]
            capacity = i["capacity"]
            phase = i["phase"]
            storage_class_name = i["storage_class_name"]
            dic = {"name":name,"namespace":namespace,"access_mode":access_mode,"capacity":capacity,"phase":phase,"storage_class_name":storage_class_name}
            models.pvc_info.objects.create(**dic)
    else:
        #pass
        for i in all_pvcs:
            name = i["name"]
            namespace = i["namespace"]
            access_mode = i["access_mode"]
            capacity = i["capacity"]
        
            phase = i["phase"]
            storage_class_name = i["storage_class_name"]
            dic = {"name": name, "namespace": name, "access_mode": access_mode, "capacity": capacity, "phase": phase,
                   "storage_class_name": storage_class_name}
        
            flag = models.pvc_info.objects.filter(name=name).exists()
            if not flag:
                models.pvc_info.objects.create(**dic)
            else:
                models.pvc_info.objects.filter(name=name).update(phase=phase)
    return True
def refresh_svc():
    all_svcs = get_services.get_svc()
    svcs = models.svc_info.objects.all()
    svc_count = svcs.count()
    if svc_count < 1:
        for i in all_svcs:
            name = i["name"]
            namespace = i["namespace"]
            cluster_ip = i["cluster_ip"]
            node_port = i["node_port"]
            port = i["port"]
            dic = {"name":name,"namespace":namespace,"cluster_ip":cluster_ip,"node_port":node_port,"port":port}
            models.svc_info.objects.create(**dic)
    else:
        #pass
        for i in all_svcs:
            name = i["name"]
            namespace = i["namespace"]
            cluster_ip = i["cluster_ip"]
            node_port = i["node_port"]
        
            port = i["port"]
            dic = {"name":name,"namespace":namespace,"cluster_ip":cluster_ip,"node_port":node_port,"port":port}
            models.svc_info.objects.create(**dic)
        
        
        
            flag = models.svc_info.objects.filter(name=name).exists()
            if not flag:
                models.svc_info.objects.create(**dic)
            else:
                models.svc_info.objects.filter(name=name).update(cluster_ip=cluster_ip)
    return True