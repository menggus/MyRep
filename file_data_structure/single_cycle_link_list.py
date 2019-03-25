class Node:
    """单项循环链表-节点"""

    def __init__(self, val):
        self.name = val
        self.next = None


class ListNode:
    """单向循环链表的实现"""

    def __init__(self, node=None):
        self._head = node  # 链表的头部
        if node:
            node.next = node

    def is_empty(self):
        """判断是否为空"""
        return self._head is None

    def length(self):
        """链表的长度"""
        cur = self._head
        if self.is_empty():
            return 0
        count = 1
        while cur.next != self._head:
            count += 1
            cur = cur.next
        return count

    def traversal(self):
        """遍历"""
        cur = self._head
        if self.is_empty():
            return 0
        while cur.next != self._head:
            print(cur.name, end=" ")
            cur = cur.next
        print(cur.name)

    def append(self, num):
        """在尾部添加元素"""
        elem = Node(num)
        if self.is_empty():
            self._head = elem
            elem.next = elem
        else:
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            cur.next = elem
            elem.next = self._head

    def add(self, num):
        """在头部位置添加元素"""
        elem = Node(num)
        cur = self._head
        if self.is_empty():
            self._head = elem
            elem.next = elem
        while cur.next != self._head:
            cur = cur.next
        elem.next = self._head
        self._head = elem
        cur.next = elem

    def insert(self, pos, num):
        """指定位置插入,单向循环链表与单向链表一样
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
        while count != pos:
            cur = cur.next
            count += 1
        elem.next = cur.next
        cur.next = elem

    def search(self, item):
        """查找节点
        ：:param item 一个val
        """
        cur = self._head
        if self.is_empty():
            return False
        while cur.next != self._head:
            if cur.name == item:
                return True
            cur = cur.next
        if cur.name == item:  # 尾节点在循环中未比较
            return True
        return False

    def remove(self, item):
        """删除节点"""
        cur = self._head
        prev = None  # 前置
        if self.is_empty():  # 链表长度为空
            return
        if cur.name == item and cur.next == self._head:  # 链表长度为1时，且删除的为该值时
            self._head = None
            return
        while cur.next != self._head:  # 链表长度大于1时
            if cur.name == item:
                if prev is None:
                    self._head = cur.next  # 当前没有循环到最后一个节点，不能设置最后一个节点的.next指向
                else:
                    prev.next = cur.next
                    return
            prev = cur
            cur = cur.next
        if cur.name == item:  # 删除value为链表的最后一个时
            prev.next = self._head
            return
        cur.next = self._head  # 删除val为链表第一个值，给最后一个节点添加指向


if __name__ == '__main__':
    listnode = ListNode()
    # print(listnode.is_empty())
    # print(listnode.length())
    # listnode.traversal()
    listnode.append(1)
    listnode.append(2)
    listnode.append(3)
    listnode.append(4)
    listnode.append(3)
    listnode.append(5)

    listnode.traversal()
    print("-"*20)
    # print(listnode.is_empty())
    # print(listnode.length())
    # listnode.traversal()
    #
    # listnode.remove(2)
    # listnode.traversal()
    #
    # print(listnode.search(0))
    #
    # listnode.add(99)
    # listnode.add(999)
    listnode.remove(3)
    listnode.traversal()
