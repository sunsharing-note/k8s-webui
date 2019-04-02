#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render,HttpResponse
# from k8s import get_nodes,get_pods,get_pv,get_namespace
from cmdb import models
import os


# def nodes(request):
#     version = models.UserInfo.objects.get(name="10.12.2.8")
#     print(version)
