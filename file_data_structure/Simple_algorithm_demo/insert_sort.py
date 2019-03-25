"""常见算法"""

# 插入算法
# list = [5, 2, 3, 4, 8, 2, 7]


def insert_sort(list):
    n = len(list)
    for j in range(1, n):
        for i in range(j):
            if list[j-i] < list[j-i-1]:
                list[j-i], list[j-i-1] = list[j-i-1], list[j-i]
            else:
                break  # 只要右边不比左边小，就退出内层循环


if __name__ == '__main__':
    list = [1, 3, 3, 6, 5, 7, 9, 8, 2, 10]
    print(list)
    insert_sort(list)
    print(list)



