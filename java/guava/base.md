# base

### Joiner
用于使用分隔符连接文本片段（特指数组，迭代器，可变参数，甚至是Map）。
如果不适用`skipNulls`或`useForNull`,则给定的元素不能包含空值，不然会抛出异常`NullPointerException`。
*连接器实例是一直不可变，且线程安全的。*

* `on` 返回一个指定了连接分割符的连接器
* `skipNulls` 返回一个自动跳过null元素的连接器
* `join` 返回连接后的字符串，以配置好间隔符间隔
* `useForNull` 返回一个连接器，当月到null元素时，使用给定的文本进行替换
* `withKeyValueSeparator` 返回一个MapJoiner，使用给定的键值分割符进行连接


### Preconditions

* `checkNotNull` 检查对象是否为空，非空时返回该对象，为空时抛出异常`NullPointerException`

