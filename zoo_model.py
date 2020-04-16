# -*- coding: utf-8 -*-
from kazoo.client import KazooClient


class ZooNode:
    def __init__(self, name):
        self.name = name


class ZooModel:
    def __init__(self):
        self.host = '127.0.0.1:2181'
        self.model = list()

    def initModel(self):
        zk = KazooClient(hosts=self.host)
        zk.start()
        zk.start()
        children = zk.get_children('/')
        for child in children:
            self.model.append(ZooNode(child))
