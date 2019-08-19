# 算法笔试面试准备

### 文件说明
Code:leetcode刷题代码

Interview:面试机器学习相关准备

### 特殊题型
1.6月1日艾耕教育实习笔试中遇到的一道题  
题目：用户在输入文本时偶尔会出错,假设给你一本结构化的词典,里面有所有词和每个词在文章中出现的频率，怎么样实现一个纠错方法。  
a.假设文本时英文单词组成，键盘敲错的概率为q，如何实现一个纠错方案？尝试用代码实现你的方案。（提示：贝叶斯定理）  
b.当文本时中文时，你上面的方案是否合适，如果假设中文是使用拼音作为输入法，上面的方案需要做什么样的调整？如果想提高准确性还需要什么信息？  

### 写的超好的经验贴
https://www.nowcoder.com/discuss/111385

### java踩过的坑（笔试注意事项）
1. 定义类的属性时用public就行，不必用static,在leetcode上用static定义的属性，调试后提交依然存在，会对提交造成干扰。

2. Long的取值范围在Long类中有属性，用Long.MIN_VALUE和LONG.MAX_VALUE调用（数值范围为-9223372036854775808 - 9223372036854775807）

3. Math.pow()方法输入可以为任意原生数据类型，但输出返回为double型，如果要计算long类型的幂函数，最好采用a\*a的形式计算，因为强制类型转换回来好像有失真，表现为输出不通过。

以上2,3来着360笔试题（城市修建）：https://www.nowcoder.com/questionTerminal/c1fa9060fae2433085e1c21f5d7e94c6?f=discussion

4. HashMap排序方法：  
HashMap的元素是Map.Entry<>  
Collections.sort不能直接对HashMap使用，需要用别的容器来存放HashMapde的Entry<>键值对，一下代码以键和值都为int型为例  
HashMap变量：map

        List<Map.Entry<Integer,Integer>> list = new LinkedList<Map.Entry<Integer,Integer>>();
        list.addAll(map.entrySet());

        Collections.sort(list, new Comparator(Map.Entry<Integer,Integer> o1, Map.Entry<Integer,Integer> o2){
          @override
          比较实体
          key的调用：o1.getKey()
          value的调用：o1.getValue()
        })

  HashMap对键的另一种排序方法：直接对keySet()排序然后再在map里查值就行

        Set keySet = map.keySet();
        Collections.sort(keySet);

        查值:for(int num:keySet) map.get(num);
