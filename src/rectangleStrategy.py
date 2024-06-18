from strategy import Strategy


# 矩形风格策略
class RectangleStrategy(Strategy):
    def __init__(self, icon_family):
        super().__init__(icon_family)
        self.width = 80     #初始化设置矩形宽度
    
    def setPrefix(self,node):
        super().setPrefix(node)
        for _ in node.parent:
            if node.isTail:
                self.prefix += '└──'
            else:
                self.prefix += '|  '
        if node.isRoot:
            self.prefix += '┌─'
        elif node.isTail:
            self.prefix += '└─'
        else:
            self.prefix += '├─'

    def setSuffix(self,node):
        super().setSuffix(node)
        length = len(self.getPrefix()+self.getNodeStr(node))
        if length < self.width:
            self.suffix += '─' * (self.width-1-length)
        if node.isRoot:
            self.suffix  += '┐'
        elif node.isTail:
            self.suffix  += '┘'
        else:
            self.suffix  += '|'