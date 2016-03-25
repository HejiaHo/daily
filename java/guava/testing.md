# testing

### NullPointerTester
一个测试用的实用程序，验证您的方法和构造函数在传递未用Nullable注释的null参数时是否会抛出NullPointerException或UnsupportedOperationException异常。
该测试方法和构造函数被调用 - 每次用一个参数为null，其余不为null。如果没有预期的抛出异常则测试失败。

* `testAllPublicStaticMethods` 执行`testMethod`于该类的所有静态公共方法，包括从父类继承的那些
* `testStaticMethods` 执行`testMethod`于该类的所有的至少`minimalVisibility`级别的方法，包括从父类继承的那些
* `testMethod` 
* `testMethodParameter` 
* `testParameter`
* `testInstanceMethods`