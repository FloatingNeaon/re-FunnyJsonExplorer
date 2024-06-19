# Re : FunnyJsonExplorer

![](D:\projects\FJE_v4\design\Class Diagram1.jpg)

- **JsonNode**:表示JSON树中的一个节点，包含节点的各种属性（如是否为根、叶子、第一节点、最后节点、尾节点等），以及节点的层级、父节点、子节点、键和值。
- **JsonNodeBuilder**:以建造者模式创建JsonNode对象，提供各种方法设置JsonNode的属性。
- **JsonParser**:解析JSON文件，并生成包含JsonNode对象的列表。
- **Strategy**:抽象策略类，用于不同的JSON节点展示风格。
- **TreeStrategy**:树形风格具体策略，继承自Strategy类，具体实现前缀和后缀的设置方法。
- **RectangleStrategy**:矩形风格策略，继承自Strategy类，具体实现前缀和后缀的设置方法。
- **FunnyJsonExplorer**:加载JSON文件并根据指定的策略显示JSON节点



### 设计模式及作用：

- 建造者模式

将构建对象`JsonNode`的复杂过程封装在建造者`JsonNodeBuilder`中，分步骤构建复杂对象

- 迭代器模式

`JsonParser`提供的`getNext()`方法和`isEnd()`方法，使调用者`FunnyJsonExplorer`能够顺序访问聚合json对象中的各个JsonNode元素，无需暴露json对象的内部表示

- 策略模式

策略类`Strategy`提供所有具体策略的通用接口，具体策略`TreeStrategy`，`RectangleStrategy`实现上下文所用算法的各种不同变体，调用者`FunnyJsonExplorer`创建一个特定策略对象并将其传递给上下文，上下文提供一个设置器使调用者在运行时替换相关联的策略