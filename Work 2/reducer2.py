#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

dataset = []

for row in sys.stdin:
    row = row.strip()
    fields = row.split('\t')

    if len(fields) == 3:
        try:
            account, search_term, amount = fields[0], fields[1], int(fields[2])
            dataset.append((account, search_term, amount))
        except ValueError:
            continue

dataset.sort(key=lambda item: item[2], reverse=True)

for account, search_term, amount in dataset[:4]:
    print("Пользователь: {}, запрос: {}, количество сделанных запросов: {}".format(account, search_term, amount))