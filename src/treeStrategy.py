"""
树形风格具体策略类
"""

from strategy import Strategy

class TreeStrategy(Strategy):
    def __init__(self, icon_family):
        super().__init__(icon_family)

    def setPrefix(self,node):
        super().setPrefix(node)
        for p in node.parent:
            if not p.isLast:
                self.prefix += '|  '
            else:
                self.prefix += '   '
        if node.isLast:
            self.prefix += '└─'
        else:
            self.prefix += '├─'
    
    def setSuffix(self,node):
        super().setSuffix(node)
