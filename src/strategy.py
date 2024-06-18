"""
抽象策略类
"""

from abc import ABC, abstractmethod
import json
class Strategy(ABC):
    def __init__(self,icon_family):
        self._loadicon(icon_family)

    def _loadicon(self,icon_family):
        with open("../icons/icon_config.json",'r',encoding='utf-8') as icon_file:
            icon_data = json.load(icon_file)
            family = icon_data[icon_family]
            self.leaf_icon = family['Leaf']
            self.container_icon = family['Container']

    def getPrefix(self):
        return self.prefix
    
    def getSuffix(self):
        return self.suffix
    
    def getNodeStr(self,node):
        if node.isLeaf:
            icon = self.leaf_icon
        else:
            icon = self.container_icon
        if node.isLeaf and node.value != '':
            return icon + str(node.key) + " : " + str(node.value)
        return icon + str(node.key)
    
    def execute(self,node):
        self.setPrefix(node)
        self.setSuffix(node)
        return self.getPrefix()+self.getNodeStr(node)+self.getSuffix()
    
    @abstractmethod
    def setPrefix(self,node):
        self.prefix = ""
    
    @abstractmethod
    def setSuffix(self,node):
        self.suffix = ""