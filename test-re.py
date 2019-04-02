#! /usr/bin/env python
# -*- coding: utf-8 -*-


import re

ret = re.search('(?P<id>\d{3})/(?P<name>\w{3})','weeew34ttt123/ooo')

print(ret.group())
print(ret.group("id"))
print(ret.group("name"))