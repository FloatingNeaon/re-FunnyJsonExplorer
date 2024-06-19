"""
json分析器类
"""

import json
from jsonNodeBuilder import JsonNodeBuilder

class JsonParser:
    def __init__(self):
        self.idx = 0
        self.jsonNodeList = []

    def reset(self):
        self.idx = 0
        self.jsonNodeList = []

    def traverse(self, nodeKV, idx, size, level, parent):
        key, value = nodeKV
        isRoot = (len(self.jsonNodeList)==0)
        isLeaf = not isinstance(value, dict)
        isFirst = (idx == 0)
        isLast = (idx == size-1)

        builder = JsonNodeBuilder()
        builder.setAttri_Root(isRoot)
        builder.setAttr_Leaf(isLeaf)
        builder.setAttri_First(isFirst)
        builder.setAttri_Last(isLast)
        builder.setAttri_Level(level)
        builder.setAttri_Parent(parent)
        builder.setAttri_Key(key)
        builder.setAttri_Value(value)

        jsonNode = builder.build()
        self.jsonNodeList.append(jsonNode)
        
        parent.append(self.jsonNodeList[-1])
        sons_idx = []
        if (isinstance(value, dict)):
            for i, n in enumerate(value.items()):
                sons_idx.append(len(self.jsonNodeList))
                self.traverse(n, i, len(value), level+1, parent)
        sons = [self.jsonNodeList[s_idx] for s_idx in sons_idx]
        builder.setAttri_Sons(sons)
        parent.pop()

    def parse(self, jsonFilePath):
        with open(jsonFilePath, 'r', encoding='utf-8') as jsonFile:
            root = json.load(jsonFile)
        self.reset()
        for i, n in enumerate(root.items()):
            self.traverse(n, i, len(root), 0, [])
        
        if len(self.jsonNodeList) > 0:
            self.jsonNodeList[-1].isTail = True

    def getNext(self):
        self.idx += 1
        return self.jsonNodeList[self.idx - 1]
    
    def isEnd(self):
        return self.idx == len(self.jsonNodeList)