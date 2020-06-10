# -*- coding: utf-8 -*-
from kazoo.client import KazooClient


class ZooNode:
    def __init__(self, name, value, zk):
        self.name = name
        self.value = value
        self.childs = list()
        self.zoo_client = zk


class ZooModel:
    def __init__(self):
        self.host = '127.0.0.1:2181'

    def initModel(self, host):
        model = list()
        self.host = host
        zk = KazooClient(hosts=self.host)
        zk.start()
        self.zoo_client = zk
        children = zk.get_children('/')
        for child in children:
            model.append(ZooNode("/"+child, zk.get("/"+child), zk))

        return model

    def get_childs(self, node_name):
        children = self.zoo_client.get_children(node_name)
        childs = list()
        for child in children:
            childs.append(
                ZooNode(node_name+"/"+child, self.zoo_client.get(node_name+"/"+child), self.zoo_client))
        return childs
