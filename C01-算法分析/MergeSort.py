def merge_sort(A):
    n = len(A)
    if n == 1:
        pass
    n_div_2 = int(n/2)
    A1 = A[0:n_div_2]
    A2 = A[n_div_2+1, n]
    merge_sort(A1)
    merge_sort(A2)

if __name__ == '__main__':
    pass