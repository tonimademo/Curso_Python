#!/usr/bin/python
# -*- coding: utf-8 -*-

from scrapy.exceptions import DropItem

import json

class Tub_ej(object):
    def __init__(self):
        self.file = open('items.jl', 'wb') # Abrimos un fichero en modo de escritura

    def process_item(self, item, spider):
        linea = json.dumps(dict(item)) + '\n'
        self.file.write(linea)
        return item
