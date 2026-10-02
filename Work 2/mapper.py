#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

for row in sys.stdin:
    elements = row.strip().split()
    
    ip = elements[0] if len(elements) > 0 else '-'
    account = elements[2] if len(elements) > 2 else '-'
    method = elements[4] if len(elements) > 4 else '-'
    endpoint = elements[5] if len(elements) > 5 else '-'
    referer = elements[8] if len(elements) > 8 else '-'

    if account == '-':
        continue

    payload = "{}|{}|{}|{}".format(ip, method, endpoint, referer)
    print("{}\t{}\t1".format(account, payload))