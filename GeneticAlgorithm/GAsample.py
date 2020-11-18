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

# 袋鼠类模拟袋鼠爬山
class Kangaroo():
    def __init__(self, genotype):
        self.genotype = self.gen_genotype(genotype)
        self.phenotype = self.genotype2phenotype()

    # 随机生成基因型
    def gen_genotype(self, genotype):
        if genotype == '':
            res_genotype = random.randint(0, 90000)
            res_genotype = format(res_genotype, 'b')
        # 返回基因型的二进制形式 不带0b
        else:
            res_genotype = genotype
        return res_genotype

    # 基因型转换为表现型
    def genotype2phenotype(self):
        phenotype = 0 + float(self.genotype*(9.0-0)/(2**17-1))
        return phenotype

    # 适应度函数
    def evl_fitness(self):
        # 这里的适应度函数就是要求的函数值
        fitness = self.phenotype+10*math.sin(5*self.phenotype)+7*math.cos(4*self.phenotype)
        return fitness

    # 基因交叉函数
    def propagation(self, Kangaroo):
        # 在交叉基因型前先将基因型还原到17位二进制
        bi_self_genotype = list(self.genotype)
        bi_Kangaroo_genotype = list(Kangaroo.genotype)
        # 使用bin转换的二进制长度不全为17位，所以求以下长度等会在交换的时候调整以下
        bi_gen_len = len(bi_self_genotype)
        bi_Kangaroo_len = len(bi_Kangaroo_genotype)
        # 填充长度到17位，从前往后填充0
        for _ in range(17-bi_gen_len):
            bi_self_genotype.insert(0, '0')
        for _ in range(17-bi_Kangaroo_len):
            bi_Kangaroo_genotype.insert(0, '0')
        # 随机交17位中的3位
        crossover_idx = random.randint(0, 15)
        for _ in range(3):
            temp = bi_self_genotype[crossover_idx]
            bi_self_genotype[crossover_idx] = bi_Kangaroo_genotype[crossover_idx]
            bi_Kangaroo_genotype[crossover_idx] = temp
            crossover_idx += 1
        # 将list转换为str
        child_genotype_1 = ''
        child_genotype_2 = ''
        # 将交叉后的基因型赋给了子类
        child_genotype_1.join(bi_self_genotype)
        child_genotype_2.join(bi_Kangaroo_genotype)
        # 生成两个子袋鼠
        return child_genotype_1, child_genotype_2

    # 基因变异
    def gen_mutate(self):
        pass