from treeStrategy import TreeStrategy
from rectangleStrategy import RectangleStrategy
from jsonParser import JsonParser
import argparse

class FunnyJsonExplorer:
    def __init__(self, strategy):
        self.parser = JsonParser()
        self.strategy = strategy

    def _load(self, jsonFilePath):
        self.jsonFilePath = jsonFilePath
        self.parser.parse(self.jsonFilePath)

    def show(self):
        while not self.parser.isEnd():
            jsonNode = self.parser.getNext()
            print(self.strategy.execute(jsonNode))


strategies = {
    "tree" : TreeStrategy ,
    "rectangle" : RectangleStrategy
}    

def main():
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-f", "--file", required=True)
    argParser.add_argument("-s", "--style", required=True)
    argParser.add_argument("-i", "--icon_family", required=True)

    args = argParser.parse_args()
    jsonFilePath = args.file
    style = args.style
    icon_family = args.icon_family

    strategy = strategies[style](icon_family)

    FJE = FunnyJsonExplorer(strategy)
    FJE._load(jsonFilePath)
    FJE.show()

if __name__ == '__main__':
    main()