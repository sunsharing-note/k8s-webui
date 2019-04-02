#! /usr/bin/env python
# -*- coding: utf-8 -*-

from os import path

from kubernetes import client,config

pvcs = []
def get_pvc():
    kube_config = path.join(path.dirname(__file__),"kubeconfig.yaml")
    config.load_kube_config(config_file=kube_config)

    v1 = client.CoreV1Api()
    # print("Listing pods with their IPs:\nname                          \taccess_modes     \tcapacity   \tphase")

    ret = v1.list_persistent_volume_claim_for_all_namespaces()
    pvcs.clear()
    for pvc in ret.items:
        status = {}
        status["name"] = pvc.metadata.name
        status["namespace"] = pvc.metadata.namespace
        status["access_mode"] = pvc.status.access_modes[0]
        status["capacity"] = pvc.status.capacity["storage"]
        status["phase"] = pvc.status.phase
        status["storage_class_name"] = pvc.spec.storage_class_name
        pvcs.append(status)
    return  pvcs
        # print("%s              \t%s         \t%s   \t%s      \t%s" % (pvc.metadata.name,pvc.status.access_modes[0],pvc.status.capacity["storage"],pvc.status.phase,pvc.spec.storage_class_name))

# if __name__ == "__main__":
#     ss = get_pvc()
#     print(ss)
