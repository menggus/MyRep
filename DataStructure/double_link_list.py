class Node:
    """双向链表-节点"""

    def __init__(self, val):
        self.name = val
        self.next = None
        self.prev = None


class ListNode:
    """双向链表的实现"""

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
        print("")

    def add(self, num):
        """在头部添加元素"""
        elem = Node(num)
        if self.is_empty():
            self._head = elem
        else:
            self._head.prev = elem
            elem.next = self._head
            self._head = elem

    def append(self, num):
        """在尾部添加元素"""
        elem = Node(num)
        if self.is_empty():
            self._head = elem
        else:
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            elem.prev = cur
            cur.next = elem

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
        while count != pos:
            cur = cur.next
            count += 1
        elem.next = cur
        elem.prev = cur.prev
        cur.prev.next = elem
        cur.prev = elem

    def search(self, item):
        """查找节点
        ：:param item 一个val
        """
        cur = self._head
        while cur is not None:
            if cur.name == item:
                return True
            cur = cur.next
        return False

    def remove(self, item):
        """删除节点"""
        cur = self._head
        while cur is not None:
            if cur.name == item:
                if cur is self._head:
                    self._head = cur.next
                    if cur.next:
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                    cur.prev = None
                    cur.next = None
                return
            cur = cur.next


if __name__ == '__main__':
    listnode = ListNode()
    print("为空?：%s, 长度：%d" % (listnode.is_empty(), listnode.length()))
    listnode.append(1)
    listnode.append(2)
    listnode.append(3)
    print("为空?：%s, 长度：%d" % (listnode.is_empty(), listnode.length()))
    listnode.traversal()
    print("-"*50)

    listnode.add(5)
    listnode.traversal()  # 头部添加：5 1 2 3

    listnode.append(1)
    listnode.traversal()  # 尾部添加：5 1 2 3 1

    listnode.insert(3, 999)
    listnode.traversal()  # 第三个位置：5 1 999 2 3 1

    print("999是否在链表中：%s" % listnode.search(999))  # 判断999是否在链表中

    listnode.remove(999)
    listnode.traversal()  # 删除999:5 1 2 3 1

