#! /usr/bin/env python
# -*- coding: utf-8 -*-

from os import path
from kubernetes import client,config

svcs = []
def get_svc():
    kube_config = path.join(path.dirname(__file__),"kubeconfig.yaml")
    #config.load_kube_config(config_file="kubeconfig.yaml")
    config.load_kube_config(config_file=kube_config)
    v1 = client.CoreV1Api()
    ret = v1.list_service_for_all_namespaces(watch=False)
    svcs.clear()
    for i in ret.items:
        status = {}
        status["name"] = i.metadata.name
        status["namespace"] = i.metadata.namespace
        status["cluster_ip"] = i.spec.cluster_ip
        status["node_port"] = i.spec.ports[0].node_port
        status["port"] = i.spec.ports[0].port
        svcs.append(status)
    return  svcs
        # print("%s \t%s \t%s \t%s \n" % ( i.metadata.name,i.metadata.namespace, i.spec.cluster_ip, i.spec.ports[0] ))
# if __name__ == "__main__":
#     get_svc()