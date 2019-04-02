#! /usr/bin/env python
# -*- coding: utf-8 -*-

import re


def get_resource(url):
    # /api/refresh/nodes?refresh=True
    ret = re.findall('/.*/.*/(\w{1,10})\?.*',url)
    return ret[0]

# if __name__ == "__main__":
#     get_resource()