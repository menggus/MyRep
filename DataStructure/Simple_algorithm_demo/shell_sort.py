"""常见算法"""

# 希尔排序


def shell_sort(alist):
    n = len(alist)
    gap = n // 2  # 希尔排序步长
    while gap >= 1:  # 最后的一次排序与插入排序一样，即gap=1时
        # 希尔排序与插入排序异同
        # 1.主要排序逻辑一样
        # 2.希尔排序加入步长概念，通过数据可寻求最优的步长

        # 下面与插入排序基本一样，唯一不同为步长gap
        for j in range(gap, n):  # 对于不同子序列，插入排序循环控制
            i = j
            while i > 0:
                if alist[i] < alist[i-gap]:
                    alist[i], alist[i-gap] = alist[i-gap], alist[i]
                    i -= gap
                else:
                    break
        gap //= 2


if __name__ == '__main__':
    alist = [3, 4, 2, 5, 7, 1, 8, 0, 9, 6]
    shell_sort(alist)
    print(alist)
