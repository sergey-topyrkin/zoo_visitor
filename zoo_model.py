# -*- coding: utf-8 -*-
from kazoo.client import KazooClient


class ZooNode:
    def __init__(self, name, zk):
        self.name = name
        self.childs = list()
        print(name)
        children = zk.get_children(name)
        for child in children:
            self.childs.append(ZooNode(name+"/"+child, zk))


class ZooModel:
    def __init__(self):
        self.host = '127.0.0.1:2181'
        self.model = list()

    def initModel(self, host):
        self.model.clear()
        self.host = host
        zk = KazooClient(hosts=self.host)
        zk.start()
        children = zk.get_children('/')
        for child in children:
            self.model.append(ZooNode("/"+child, zk))
