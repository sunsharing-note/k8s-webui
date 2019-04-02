#! /usr/bin/env python
# -*- coding: utf-8 -*-

from os import path
from kubernetes import client,config

pod = []
def get_pods():

    kube_config = path.join(path.dirname(__file__),"kubeconfig.yaml")
    #config.load_kube_config(config_file="kubeconfig.yaml")
    config.load_kube_config(config_file=kube_config)
    v1 = client.CoreV1Api()
    # print("Listing pods with their IPs:")
    ret = v1.list_pod_for_all_namespaces(watch=False)
    # for i in ret.items:
    #     print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
    pod.clear()
    for i in ret.items:
        status = {}
        status["pod_ip"] = i.status.pod_ip
        status["namespace"] = i.metadata.namespace
        status["name"] = i.metadata.name
        status["status"] = i.status.phase
        pod.append(status)
    return pod
#         print(pod)
# if __name__ == "__main__":
#     ss = get_pods()
#     print(type(ss))
