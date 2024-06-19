# Re : FunnyJsonExplorer



- **JsonNode**:表示JSON树中的一个节点，包含节点的各种属性（如是否为根、叶子、第一节点、最后节点、尾节点等），以及节点的层级、父节点、子节点、键和值。
- **JsonNodeBuilder**:以建造者模式创建JsonNode对象，提供各种方法设置JsonNode的属性。
- **JsonParser**:解析JSON文件，并生成包含JsonNode对象的列表。
- **Strategy**:抽象策略类，用于不同的JSON节点展示风格。
- **TreeStrategy**:树形风格具体策略，继承自Strategy类，具体实现前缀和后缀的设置方法。
- **RectangleStrategy**:矩形风格策略，继承自Strategy类，具体实现前缀和后缀的设置方法。
- **FunnyJsonExplorer**:加载JSON文件并根据指定的策略显示JSON节点



### 设计模式及作用：

- 建造者模式

将构建对象的复杂过程封装在建造者中，分步骤构建复杂对象