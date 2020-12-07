from MyStack import MyStack
import random

def merge_sort(A):
    # if n == 1, done
    n = len(A)
    if n == 1:
        return A
    A1 = A[0:int(n/2)]
    A2 = A[int(n/2):]
    A1.sort()
    A2.sort()
    # "merge" the 2 sorted lists
    A1 = MyStack(A1)
    A2 = MyStack(A2)
    # 对于n个数字
    # B = []
    for i in range(n):
        a1 = A1.peek()
        a2 = A2.peek()
        if a1 == None:
            # 此时n次还没有执行完，所以a2一定不为空
            A[i] = a2
            # B.append(a2)
            A2.pop()
        elif a2 == None:
            # 此时n次还没有执行完，所以a1一定不为空
            A[i] = a1
            # B.append(a1)
            A1.pop()
        else:
            if a1 < a2:
                A[i] = a1
                # B.append(a1)
                A1.pop()
            else:
                A[i] = a2
                # B.append(a2)
                A2.pop()
    return A
if __name__ == "__main__":
    A = [x for x in range(100)]
    print('Original list are: {}'.format(A))
    random.shuffle(A)
    print('After random.shuffle(): {}'.format(A))
    A = merge_sort(A)
    print('After merge_sort(): {}'.format(A))