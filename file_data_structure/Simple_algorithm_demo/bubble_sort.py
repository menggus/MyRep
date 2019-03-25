"""常见的排序算法"""

# 冒泡排序
# list = [5, 2, 3, 4, 8, 2, 7]


def bubble_sort(list):
    n = len(list)
    for i in range(n-2):
        # 主题循环结构
        for j in range(n-1-i):
            if list[j] > list[j+1]:
                list[j+1], list[j] = list[j], list[j+1]
        print("执行第%s次：%s" % (i, list))


if __name__ == '__main__':
    list = [5, 2, 3, 4, 8, 2, 7]
    print(list)
    bubble_sort(list)
    print(list)


