from django.db import models

# Create your models here.

class UserInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    role = models.CharField(max_length=64)
    version = models.CharField(max_length=64)
    status = models.CharField(max_length=64)
    
class pods_info(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    ip = models.CharField(max_length=64)
    namespace = models.CharField(max_length=64)
    status = models.CharField(max_length=64)

'''
status["name"] = pv.metadata.name
        status["capacity"] = pv.spec.capacity["storage"]
        status["access_modes"] = pv.spec.access_modes[0]
        status["persistent_volume_reclaim_policy"] = pv.spec.persistent_volume_reclaim_policy
        status["status"] = pv.status.phase
        status["storage_class_name"] = pv.spec.storage_class_name
'''
class pvs_info(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    capacity = models.CharField(max_length=64)
    access_modes = models.CharField(max_length=64)
    persistent_volume_reclaim_policy = models.CharField(max_length=64)
    status = models.CharField(max_length=64)
    storage_class_name = models.CharField(max_length=64)
"""
models.pods_info.objects.create(
            name = name,
            ip = ip,
            namespace = namespace,
            status = status,
        )
"""
class namespace_info(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)


"""
status["name"] = pvc.metadata.name
status["access_mode"] = pvc.status.access_modes[0]
status["capacity"] = pvc.status.capacity["storage"]
status["phase"] = pvc.status.phase
status["storage_class_name"] = pvc.spec.storage_class_name
"""

class pvc_info(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    namespace = models.CharField(max_length=64)
    access_mode = models.CharField(max_length=64)
    capacity = models.CharField(max_length=64)
    phase = models.CharField(max_length=64)
    storage_class_name = models.CharField(max_length=64)

"""
        status["name"] = i.metadata.name
        status["namespace"] = i.metadata.namespace
        status["cluster_ip"] = i.spec.cluster_ip
        status["node_port"] = i.spec.ports[0].node_port
        status["port"] = i.spec.ports[0].port
"""
class svc_info(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    namespace = models.CharField(max_length=64)
    cluster_ip = models.CharField(max_length=64,null=True)
    node_port = models.CharField(max_length=64,null=True)
    port = models.CharField(max_length=64,null=True)