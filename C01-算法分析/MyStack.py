# -*- coding:utf-8 -*-
# __author__ :kusy
# __content__:文件说明
# __date__:2018/9/30 17:28


class MyStack(object):
    def __init__(self, alist=None):
        if alist == None:
            self.stack_list = []
            self.count = 0
        else:
            self.stack_list = alist
            self.count = len(alist)

    # 栈中添加值
    def push(self, value):
        self.stack_list.insert(0,value)
        self.count += 1

    #返回栈顶元素值
    def peek(self):
        if self.count:
            return self.stack_list[0]
        return None

    # 删除栈顶元素
    def pop(self):
        self.stack_list.pop(0)
        self.count -= 1

    # 返回栈是否为空
    def is_empty(self):
        if self.count == 0:
            return True
        else:
            return False 

    #打印栈内容
    def print_all(self):
        for sl in self.stack_list:
            print(sl)