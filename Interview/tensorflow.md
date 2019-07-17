# Tensorflow

### 请简要介绍下tensorflow的计算图
tensorflow是一个通过计算图的形式来表述计算的编程系统，计算图也叫数据流图，可以吧计算图看做是一种有向图，Tensorflow中的每一个节点都是计算图上的一个Tensor，也就是张量，而节点之间的边描述了计算之间的依赖关系（定义时）和数学操作（运算时）。

### tf.Variable()和tf.get_Variable()的区别
参考：https://blog.csdn.net/timothytt/article/details/79789274  

二者的本质区别在于，当出现name冲突时处理不同。  

使用tf.Variable()的时候，出现变量名字冲突，框架会自动修改，处理方式是加下划线编号，如：  

    var1 = tf.Variable(initial_value=0.0, name="var")
    var2 = tf.Variable(initial_value=0.1, name="var")
    
那么var1的名字还是“var”，但var2的名字会变成“var_1”  

tf.get_Variable()依据命名空间是否开启自动变量复用来处理，不开启出现冲突时会报错；开启后冲突的变量内容都是第一个赋值的那个变量。

    注：开启变量复用的方式如下  
    with tf.variable_scope("scope1",reuse=tf.AUTO_REUSE):
      ……
