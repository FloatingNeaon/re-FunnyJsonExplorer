"""
以建造者模式生成节点
"""

from jsonNode import JsonNode

class JsonNodeBuilder:
    def __init__(self):
        self.node = JsonNode()

    def setAttri_Root(self, isRoot):
        self.node.isRoot = isRoot

    def setAttr_Leaf(self, isLeaf):
        self.node.isLeaf = isLeaf

    def setAttri_First(self, isFirst):
        self.node.isFirst = isFirst

    def setAttri_Last(self, isLast):
        self.node.isLast = isLast

    def setAttri_Level(self, level):
        self.node.level = level

    def setAttri_Parent(self, parent):
        self.node.parent = parent.copy()

    def setAttri_Sons(self, sons):
        self.node.sons = sons

    def setAttri_Key(self, key):
        self.node.key = key

    def setAttri_Value(self, value):
        if value == None:
            self.node.value = ""
        else :
            self.node.value = value
    
    def build(self):
        return self.node