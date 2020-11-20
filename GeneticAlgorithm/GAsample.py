# !/usr/bin/python
# -*- coding:utf-8 -*-  
# @author: Dongsheng li
# @date: 2020-11-18 Wednesday
# @email: lids@mail.hfut.edu.cn
#
# Genetic Algorithm Optimization in Pytorch
#
# We are going to implement a genetic algorithm to optimize to find out the maximum value of the function 
# f(x)=x+10sin(5x)+7cos(4x)
# in the range [0, 9].

import random
import math

UPPER_LIMIT = 9
LOWER_LIMIT = 0
PRECISION = 4
NUM_GEN_CROSS = 7
PROB_OF_MUTATE = 0.4
# 变异基因的个数
NUM_OF_MUTATE = 5
# 注意 为了方便两两配对，种群数量POPULATION只能为偶数个
POPULATION = 1000
ITERATION = 20

# 基因序列数目，根据上下限和精度分配
num_gens = math.ceil(math.log2((UPPER_LIMIT-LOWER_LIMIT)*pow(10, PRECISION)))

# 袋鼠类模拟袋鼠爬山
class Kangaroo():
    def __init__(self, genotype):
        self.genotype = self.gen_genotype(genotype)
        self.phenotype = self.genotype2phenotype()
        self.fitness = self.evl_fitness()

    # 随机生成基因型
    def gen_genotype(self, genotype):
        if genotype == None:
            res_genotype = random.randint(0, (UPPER_LIMIT-LOWER_LIMIT)*pow(10,PRECISION))
            res_genotype = format(res_genotype, 'b')
        # 返回基因型的二进制形式 不带0b
        else:
            res_genotype = genotype
        # 将基因型填充为num_gens位
        bi_genotype = list(res_genotype)
        res_genotype = ''
        for _ in range(num_gens-len(bi_genotype)):
            bi_genotype.insert(0, '0')
        res_genotype = res_genotype.join(bi_genotype)
        assert len(res_genotype) == num_gens
        return res_genotype

    # 基因型转换为表现型
    def genotype2phenotype(self):  
        phenotype = 0 + (int(self.genotype, 2)*(UPPER_LIMIT-LOWER_LIMIT))/(pow(2,num_gens)-1)
        return phenotype

    # 适应度函数
    def evl_fitness(self):
        # 这里的适应度函数就是要求的函数值
        fitness = self.phenotype+10*math.sin(5*self.phenotype)+7*math.cos(4*self.phenotype)
        return fitness

    # 基因交叉函数
    def gen_crossover(self, genotype):
        bi_self_genotype = list(self.genotype)
        bi_Kangaroo_genotype = list(genotype)

        # 随机交num_gens位中的NUM_GEN_CROSS位
        crossover_idx = random.randint(0, num_gens-NUM_GEN_CROSS-1)
        for _ in range(4):
            temp = bi_self_genotype[crossover_idx]
            bi_self_genotype[crossover_idx] = bi_Kangaroo_genotype[crossover_idx]
            bi_Kangaroo_genotype[crossover_idx] = temp
            crossover_idx += 1
        # 将list转换为str
        child_genotype_1 = ''
        child_genotype_2 = ''
        # 将交叉后的基因型赋给了子类
        assert len(child_genotype_1) == 0
        res_1 = child_genotype_1.join(bi_self_genotype)
        res_2 = child_genotype_2.join(bi_Kangaroo_genotype)
        # 生成两个子袋鼠的基因型
        # print(res_1, res_2)
        return res_1, res_2

    # 基因变异
    def gen_mutate(self, genotype):

        # 以PROB_OF_MUTATE的概率选择一个index
        res = genotype
        # 以PROB_OF_MUTATE的概率决定是否变异
        is_mutate = random.choices([True, False], weights=[PROB_OF_MUTATE, 1-PROB_OF_MUTATE], k=1)
        
        # 增加基因变异次数
        for _ in range(NUM_OF_MUTATE):
            # 即是基因型从0到1或者从1到0的转变
            if is_mutate == True:
                idx = random.randint(0, num_gens-1)
                list_genotype = list(genotype)
                if list_genotype[idx] == '0':
                    list_genotype[idx] = '1'
                else:
                    list_genotype[idx] = '0'
                mutate_gen = ''
                res = mutate_gen.join(list_genotype)
                genotype = res
        return res
        
    # 产生子袋鼠
    def propogation(self, genotype):
        return Kangaroo(genotype)


# 创建一个族群里面有POPULATION个袋鼠
kan_group = []
for _ in range(POPULATION):
    genotype = random.randint(0, (UPPER_LIMIT-LOWER_LIMIT)*pow(10, PRECISION))
    genotype = format(genotype, 'b')
    a = Kangaroo(genotype)
    # print(a.genotype)
    kan_group.append(a)

for j in range(ITERATION):
    # 保证族群数量为POPULATION
    assert len(kan_group) == POPULATION
    # 从中按序号进行配对，因为本身的基因型是随机的，所以相邻序号不会有问题        
    for i in range(0,POPULATION,2):
        # 基因型在父代间的繁殖中发声交叉
        kan_gen1, kan_gen2 = kan_group[i].gen_crossover(kan_group[i+1].genotype)
        # 基因型在父代间繁殖时中发生变异
        kan_gen1 = kan_group[i].gen_mutate(kan_gen1)
        kan_gen2 = kan_group[i].gen_mutate(kan_gen2)
        # 变异后的的基因生成新的袋鼠加入到族群中
        kan_child1 = kan_group[i].propogation(kan_gen1)
        kan_child2 = kan_group[i].propogation(kan_gen2)
        kan_group.append(kan_child1)
        kan_group.append(kan_child2)
        # 如此一来族群就增加了POPULATION个新生命，

    # 现在通过kangaroo的fitness值判断是否需要从族群中去除
    # 为了维持族群总的袋鼠数量不变，所以需要杀掉一半的袋鼠
    # 选择方法为精英选择制度，即适应度最高的留下
    kan_group_fitness = {}
    kan_group_dic = {}
    # 创建整个族群的fitness字典
    for i in range(2*POPULATION):
        kan_group_dic[i] = kan_group[i]
        kan_group_fitness[i] = kan_group[i].fitness
    # 对字典按照fitness值进行排序
    order_kg_fitness = sorted(kan_group_fitness.items(), key=lambda x:x[1])
    # 打印此次循环后的最大值
    print('idx: {}, value: {}'.format(j+1, order_kg_fitness[len(order_kg_fitness)-1][1]))
    # 根据idx从族群中除去fitness较小的袋鼠
    for i in range(POPULATION):
        # 只除去一半的袋鼠
        idx = order_kg_fitness[i][0]
        del kan_group_dic[idx]
    # 用新的族群去代替就的group_list
    kan_group.clear()
    for value in kan_group_dic.values():
        kan_group.append(value)
    # 打乱kan_group的顺序
    random.shuffle(kan_group)