"""
Json节点类
"""

class JsonNode:
    def __init__(self):
        self.isRoot = False
        self.isLeaf = False
        self.isFirst = False
        self.isLast = False
        self.isTail = False
        self.parent = None
        self.sons = None
        self.level = None
        self.key = None
        self.value = None
    