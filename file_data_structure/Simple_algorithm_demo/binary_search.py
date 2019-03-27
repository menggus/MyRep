"""常见算法"""

# 二分查找法


# 递归
def binary_search(alist, val):
    n = len(alist)
    mid = n // 2
    if n < 1:
        return False
    if alist[mid] == val:
        return True
    elif alist[mid] > val:
        print("mid = %s" % mid)
        return binary_search(alist[0:mid], val)

    elif alist[mid] < val:
        print("mid = %s" % mid)
        return binary_search(alist[mid+1:], val)


# 非递归
def binary_search_two(alist, val):
    i, j = 0, len(alist)-1
    while i <= j:
        mid = (i+j) // 2
        if alist[mid] == val:
            return True
        elif alist[mid] > val:
            j = mid-1
        elif alist[mid] < val:
            i = mid+1

    return False


if __name__ == '__main__':
    alist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    # bool = binary_search(alist, 10)
    bool_tow = binary_search_two(alist, 2)
    # print(bool)
    print(bool_tow)
