# Logistic Regression
LR是一个对数线性模型。
## 重要的参考资料
1.简书上的一篇博文，介绍了LR的推导、原理及优缺点  
    https://www.jianshu.com/p/e8dca5613da6  
2.比1讲解的更好一点  
    https://blog.csdn.net/qq_32742009/article/details/81516140  
## 1. LR的原理
y = Wx为线性回归模型，其中W=[w1,,w2,……,wn,b]，在线性回归模型特征到结果的映射中加上Sigmoid函数（即y = 1/(1+e^(-Wx))），使输出映射到[0,1]区间内，用于处理二分类问题的模型即为逻辑斯蒂回归模型。
## 2. LR的求解数学推导
LR的数学推导指的是LR参数估计公式的推导过程，也即用极大似然估计LR模型的参数的推导过程，详见参考资料1中3.2
## 3. LR的正则化
参考资料2中有简略的，还需要寻找更详细的
## 4. 为什么LR能比线性回归好
参考资料2中有
## 5. LR与MaxEnt的关系

## 6. 并行化的LR
https://blog.csdn.net/qq_32742009/article/details/81839071 （还没完全看懂）

## 7. LR的学习方法
通俗讲解牛顿法 https://blog.csdn.net/ccnt_2012/article/details/81837154  
牛顿法及拟牛顿法 https://blog.csdn.net/songbinxu/article/details/79677948  
