
"""
    给定一个整型数组A, 以及一个整数M, 判断A中是否存在i, j, 使得
            M = A[i] + A[j]

    排序 + 二分查找
"""
# 数据
A = [7, 6, 4, 3, 2, 1, 8, 9, 5]
M = 9


# 解法一: 暴力枚举法
def getij(a, m):
    dictij = list()
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if i !=j and M == a[i] + a[j]:
                dictij.append((i, j))
                print(i, j)
    return dictij


# 解法二: enumerate
# enumerate: 序列化
def enum(a, m):
    res = dict()
    for k, v in enumerate(a): # n

        if m-v in res:

            return res.get(m-v), k
        res[v] = k
        # print(res)


# 解法三: 利用排序与二分查找, 二分查找条件: 由于操作的为下标, 所以要求查找的容器为 顺序表
def binaryfind(a, m):
    """
        二分查找-递归
    :param a: 列表
    :param m: 查找值
    :return: i 找到值的索引, -1 未找到
    """
    if len(a) == 0:
        return -1
    i = int(len(a)/2)
    if a[i] == m:
        return i
    if a[i] > m:
        return binaryfind(a[i+1:], m)
        # 这里是否需要关注i+1的值与len(a)的值吗
        #  and i+1 < len(a) 关于切片操作中的index问题, 如果切片的范围不在列表索引内不会报错, 超出范围内的索引切片值为空列表
    if a[i] < m:
        return binaryfind(a[0:i], m)
    return -1


def binaryfinds(a, m):
    """
        二分查找- 非递归
    :param a: 查找列表
    :param m: 查找元素
    :return: mid查找列表元素的索引, -1 未找到
    """
    if len(a) == 0:
        return -1
    first = 0
    last = len(a)-1
    while first <= last:
        mid = (last+first)//2
        if a[mid] == m:
            return mid
        if a[mid] < m:
            first = mid + 1
        if a[mid] > m:
            last = mid - 1
    return -1


if __name__ == '__main__':
    # getij(A, M)

    # enum(A, M)
    a = [1,2,3,4]
    res = binaryfinds(a, 3)
    print(res)