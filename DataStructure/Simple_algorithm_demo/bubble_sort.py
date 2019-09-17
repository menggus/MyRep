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

def bubble_sort_2(alist):
    """
        冒泡排序
        原理: 遍历元素, 对比当前元素和后一个元素, 并交换元素位置, 来达到排序目的;
    :param alist: 排序的列表
    :return: 排好序的列表
    """
    length = len(alist)
    if length <= 1:

        return alist
    j = 0
    while j < length-1:
        i = 0
        while i < length-1-j:  # 这里减掉j可以减少遍历次数
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
            i += 1
        j += 1
        print(i)

    return alist


if __name__ == '__main__':
    list = [5, 2, 3, 4, 8, 2, 7]
    print(list)
    bubble_sort(list)
    print(list)


