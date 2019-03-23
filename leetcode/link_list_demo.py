class Node:
    """链表-节点"""

    def __init__(self, val):
        self.name = val
        self.next = None


class ListNode:
    """链表的实现"""

    def __init__(self, node=None):
        self._head = node  # 链表的头部

    def is_empty(self):
        """判断是否为空"""
        return self._head is None

    def length(self):
        """链表的长度"""
        cur = self._head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def traversal(self):
        cur = self._head
        while cur is not None:
            print(cur.name, end=" ")
            cur = cur.next

    def append(self, num):
        """在尾部添加元素"""
        elem = Node(num)
        if self.is_empty():
            self._head = elem
        else:
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            cur.next = elem

    def add(self, num):
        """在指定位置添加元素"""
        elem = Node(num)
        elem.next = self._head
        self._head = elem

    def insert(self, pos, num):
        """指定位置插入
        :param pos 表示插入位置 ，从0开始
        ：:param num 表示插入的链表的值
        """
        elem = Node(num)
        if pos <= 0:
            self.add(num)
            return
        if pos > self.length():
            self.append(num)
            return
        cur = self._head
        count = 1
        # while cur is not None:
        #     if count == pos:
        #         elem.next = cur.next
        #         cur.next = elem
        #         return
        #     cur = cur.next
        #     count += 1
        while count != pos:
            cur = cur.next
            count += 1
        elem.next = cur.next
        cur.next = elem


if __name__ == '__main__':
    listnode = ListNode()
    # print(listnode.is_empty())
    # print(listnode.length())
    listnode.append(1)
    listnode.append(2)
    listnode.append(3)
    listnode.append(4)
    listnode.append(5)
    listnode.append(6)
    listnode.traversal()
    print()
    listnode.insert(8, 99)
    listnode.traversal()
