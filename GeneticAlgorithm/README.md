# Genetic Algorithm Sample
> 遗传算法，暂时在课堂中还没有涉及，因为实验需要，先写一个sample在这里
### Help you understand
- [遗传算法基础](https://www.zhihu.com/question/23293449/answer/120220974?utm_source=wechat_session)
- [射杀代数的例子](https://blog.csdn.net/u010451580/article/details/51178225/)
- [交叉算子小结](https://blog.csdn.net/u012750702/article/details/54563515)

问题：求解函数f(x) = x + 10*sin(5*x) + 7*cos(4*x) 在区间[0,9]的最大值
**********
### Hyper Parameters
Hyper Parameters|Explanation
---|---
UPPER_LIMIT|自变量上限
LOWER_LIMIT|自变量下限
PRECISION|求解精度
NUM_GEN_CROSS|基因交叉数目
PROB_OF_MUTATE|基因变异概率
NUM_OF_MUTATE|基因变异的个数
POPULATION|种群数量
ITERATION|迭代次数
***********
### Incomplete Solutions
- 基因序列选择的二进制方案，不够多变
- 交叉基因部分紧挨，对于基因改变不够大
- 变异方法采用重复多次的方案，有可能多次变到同一个基因，但是没有察觉，在二进制基因型中是非常致命的，因为同一个基因可能从0变1，然后再次被选中，从1变成0，这样就相当于没有变化，而且将基因突变概率设置的越大，越容易产生这样的坑（暂时没有时间填了）
- 选择制使用了`精英方案`，但是变异方法又不够完善，所以还是会有概率求到局部极值
