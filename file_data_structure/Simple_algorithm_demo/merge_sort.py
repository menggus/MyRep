"""常见算法"""

# 归并排序
"""
对列表进行归并排序 alist = [5, 3, 2, 1, 4, 6]
       首先对列表进行如下拆分操作,按 mid = len(alist) // 2
           5 3 2 1 4 6  
                     
        5 3 2       1 4 6
      5    3 2     1   4 6    
    5     3   2   1   4   6    # 形成单一元素

    按拆分的逆序进行归并操作，创建一个新的列表进行接收
    判断左右两个列表各元素的值，小的值先往新列表进行append()操作，循环操作至归并成一个列表
    
    操作完成形成有序列表；
     
"""


def merge_sort(alist):

    n = len(alist)
    if n <= 1:
        return alist
    mid = n // 2  # 进行区分的中间值
    left_merge = merge_sort(alist[:mid])  # 对左边序列进行递归，直到最后只有一个元素
    right_merge = merge_sort(alist[mid:])  # 对右边序列进行递归，直到最后只有一个元素

    left, right = 0, 0  # 左右两个游标
    result_li = []
    while left < len(left_merge) and right < len(right_merge):
        # 通过两个游标left，right对左右顺序进行逻辑排序
        if left_merge[left] > right_merge[right]:
            result_li.append(right_merge[right])
            right += 1
        else:
            result_li.append(left_merge[left])
            left += 1
    result_li += left_merge[left:]
    result_li += right_merge[right:]
    return result_li


if __name__ == '__main__':
    alist = [2, 4, 5, 3, 1, 7, 6, 8, 0]
    li = merge_sort(alist)
    print(li)
