# 插入排序算法
import random   # 用于打乱顺序

def insertion_sort(A,   # 需要排序的序列A
                   n):  # 序列A的长度n
    # 循环从第2个元素开始，即是A[1]，需要循环n-1次，在python中的表达即为range(1, n)
    for j in range(1, n):
        key = A[j]
        i = j-1
        # 当前一个大于后一个即交换前后两个元素，直到key元素大于前一个元素为止
        while i>=0 and A[i]>key:
            A[i+1] = A[i]
            i = i-1
        # 在循环内部做比较的时候将i设置成了i-1，而循环结束后key的位置应该是i+1
        A[i+1] = key

if __name__ == '__main__':
    # 创建一个有序数组A
    A = [x for x in range(10)]
    print(A)
    # 将数组A打乱
    random.shuffle(A)
    print(A)
    # 调用插入排序算法查看效果
    insertion_sort(A, len(A))
    print(A)