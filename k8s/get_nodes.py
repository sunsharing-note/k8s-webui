#! /usr/bin/env python
# -*- coding: utf-8 -*-

from os import path
from kubernetes import client,config

node = []

def get_node():

    kube_config = path.join(path.dirname(__file__),"kubeconfig.yaml")
    #config.load_kube_config(config_file="kubeconfig.yaml")
    config.load_kube_config(config_file=kube_config)
    #config.kube_config.load_kube_config(config_file="kubeconfig.yaml")
    v1 = client.CoreV1Api()
    #print("Listing All nodes with their info:\nname    \trole \tversion")
    ret = v1.list_node()
    node.clear()
    for i in ret.items:
        #node[i.metadata.name] = i.metadata.labels["kubernetes.io/role"]
        # print(node.values())
        status = {}
        status["name"] = i.metadata.name
        status["role"] = i.metadata.labels["kubernetes.io/role"]
        status["version"] = i.status.node_info.kubelet_version
        status["status"] = i.spec.unschedulable
        # (i.status.conditions).sort()
        # print("11111",i.status.conditions)
        # print(status)
        
        node.append(status)
    # return i.metadata.name,i.metadata.labels["kubernetes.io/role"],i.status.node_info.kubelet_version
    # print(node)
    return node
#         return ("%s \t%s \t%s \t" % (i.metadata.name,i.metadata.labels["kubernetes.io/role"],i.status.node_info.kubelet_version))
# if __name__ == "__main__":
#     ss = get_node()

# if __name__ == "__main__":
#     ss = get_node()
#     print(ss)if __name__ == "__main__":
# #     ss = get_node()
# #     print(ss)