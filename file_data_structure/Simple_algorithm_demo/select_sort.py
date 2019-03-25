"""常见的排序算法"""

# 选择排序
# li = [1,3,4,2,8,5,4]


def select_sort(lis):
    n = len(lis)
    for j in range(n-2):
        min_index = j
        for i in range(j+1, n):
            if lis[min_index] > lis[i]:
                min_index = i
        lis[j], lis[min_index] = lis[min_index], lis[j]
        print("第%s次： %s " % (j, lis))


if __name__ == '__main__':
    li = [1, 3, 4, 2, 8, 5, 4]
    select_sort(li)
    print(li)
