#! /usr/bin/env python
# -*- coding: utf-8 -*-

from os import path

from kubernetes import client,config

pvs = []
def get_pv():
    kube_config = path.join(path.dirname(__file__),"kubeconfig.yaml")
    config.load_kube_config(config_file=kube_config)

    v1 = client.CoreV1Api()
#     print("Listing pods with their IPs:\nname        \t状态")

    ret = v1.list_persistent_volume()
    pvs.clear()
    for pv in ret.items:

        status = {}
        status["name"] = pv.metadata.name
        status["capacity"] = pv.spec.capacity["storage"]
        status["access_modes"] = pv.spec.access_modes[0]
        status["persistent_volume_reclaim_policy"] = pv.spec.persistent_volume_reclaim_policy
        status["status"] = pv.status.phase
        status["storage_class_name"] = pv.spec.storage_class_name
        pvs.append(status)
    return pvs
     

        # print("%s     \t%s" % (pv.metadata.name,pv.status.phase))      \t%s     \t%s     \t%s     \t%s     
        # print("%s     \t%s     \t%s      \t%s      \t%s      \t%s" % (pv.metadata.name,pv.spec.capacity["storage"],pv.spec.access_modes[0],pv.spec.persistent_volume_reclaim_policy,pv.status.phase,pv.spec.storage_class_name))

# if __name__ == "__main__":
#     main()
