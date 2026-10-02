#!/usr/bin/env python

import sys

data_store = {}

for row in sys.stdin:
    row = row.strip()
    fields = row.split('\t')
    
    if len(fields) != 3:
        continue

    account, request, amount_str = fields[0], fields[1], fields[2]
    
    try:
        amount = int(amount_str)
    except ValueError:
        continue

    pair = (account, request)
    data_store[pair] = data_store.get(pair, 0) + amount

for (account, request), total in data_store.items():
    print("{}\t{}\t{}".format(account, request, total))