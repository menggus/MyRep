"""常见算法"""

# 快速排序


def quick_sort(alist, first, end):
    if first >= end:  # 递归的结束条件，列表只有一个元素时候
        return
    low = first
    high = end
    mid_value = alist[first]
    while low < high:
        # 具体判断逻辑
        while low < high and alist[high] >= mid_value:  # “等号”是让相等的值，在分的时候处在同一边
            high -= 1
        alist[low] = alist[high]
        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]
    alist[low] = mid_value
    print("执行每一次：%s" % alist)
    quick_sort(alist, first, low-1)  # 对从mid_value区分的左边list进行递归排序
    quick_sort(alist, low+1, end)  # 对从mid_value区分的右边list进行递归排序


if __name__ == '__main__':
    alist = [5, 2, 4, 6, 8, 3, 1, 9]
    quick_sort(alist, 0, len(alist)-1)
    print(alist)
