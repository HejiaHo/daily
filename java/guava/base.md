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
Gauva提供的一些先决条件检查实用。
每个方法都有下面三张形式
* 无参数。异常抛出时不带错误信息
* 一个`Object`参数。异常抛出时带有错误信息`object.toString()`
* 一个`String`参数，及任意个附加的`Object`参数，有点类似printf。使用方法类似于：
`checkArgument(i >= 0, "Argument was %s but expected nonnegative", i);
checkArgument(i < j, "Expected i < j, but %s > %s", i, j);
`

* `checkArgument` 检查表达式的结果是否为true。为false时抛出异常`IllegalArgumentException`
* `checkNotNull` 检查对象是否为空，非空时返回该对象，为空时抛出异常`NullPointerException`
* `checkState` 检查对象的状态是否为true。为false时抛出异常`IllegalStateException`
* `checkElementIndex` 检查下标在数组、列表或字符串的长度中是否有效。下标为负数或不小于长度时抛出异常`IndexOutOfBoundsException`。长度为负时抛出异常`IllegalArgumentException`。
* `checkPositionIndex` 检查下标在数组、列表或字符串的长度中是否有效。下标为负数或大于长度时抛出异常`IndexOutOfBoundsException`。长度为负时抛出异常`IllegalArgumentException`。
* `checkPositionIndexs` 检查起始和结束下标在数组、列表或字符串的长度中是否有效且是否有序。下标为负数或大于长度、或结束下标小于开始下标时抛出异常`IndexOutOfBoundsException`。长度为负时抛出异常`IllegalArgumentException`。


