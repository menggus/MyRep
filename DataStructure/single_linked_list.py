# 单链表

class Node:
    """节点"""
    def __init__(self, data, next=None):
        """
            初始化
        :param data: 节点值
        :param next: 下一个节点地址
        """
        self.data = data
        self.next = next

    def __str__(self):

        return self.data


class SingleLinkList:
    """单链表"""
    def __init__(self):
        # 链表头部
        self.head = None

    def append(self, val):
        """
            添加值
            1. 判断链表是否为空
                - 为空, 直接把self.head指向新建节点
            2. 遍历链表找到最后节点
                - 条件, node.next == None
                - 最后节点的node.next 指向新建节点
        :param node: 节点
        :return: True or False
        """
        node = Node(val)
        if not self.head:
            self.head = node
            return

        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

    def insert(self, val, k):
        """
            在第k个节点位置插入, k从0开始(下标对应)
            1. 遍历到k-1节点位置
            2. 新节点next指向当前节点的next
            3. 当前节点的next指向新节点
        :param val:
        :param k:
        :return:
        """
        node = Node(val)
        if k < 0:
            raise ValueError("k值错误 >= 0")
        if k == 0:
            node.next = self.head
            self.head = node
            return
        if k > self.length-1:

            self.append(val)
            return

        cur = self.head
        n = 0
        while n+1 != k:
            cur = cur.next
            n += 1
        node.next = cur.next
        cur.next = node
        return

    def remove(self, val):
        """删除值为val的节点"""
        if not self.head:
            raise ValueError("linklist.remove(x): x not in linklist")
        if self.head.data == val:
            self.head = self.head.next
            return

        cur = self.head
        while cur.next:
            if cur.next.data == val:
                cur.next = cur.next.next
                return
            cur = cur.next

        raise ValueError("linklist.remove(x): x not in linklist")

    @property
    def length(self):
        """链表的长度"""
        if not self.head:
            return 0
        cur = self.head
        n = 0
        while cur:
            n += 1
            cur = cur.next
        return n

    def print_all(self):
        """
            打印链表值
            1. 链表为空, 直接打印None
            2. 不为空, 遍历打印node.data
        """
        if not self.head:
            print("None")
            return
        cur = self.head

        while cur.next:
            print(cur.data, end=" ")
            cur = cur.next
        print(cur.data)

    def __str__(self):
        """
            关于最后返回值, 是采用列表拼接还是字符串拼接的问题

            jion的方式比字符串的 拼接操作(+) 效率更高, 字符串(不可变类型)拼接操作需要重新申请内存
        :return:
        """
        if not self.head:
            return None
        cur = self.head
        link = []
        # link = ""
        while cur.next:
            link.append(cur.data.__str__())
            # link += cur.data.__str__() + " "  # 字符串拼接
            cur = cur.next
        link.append(cur.data.__str__())
        # link += cur.data.__str__() + " "
        return " ".join(link)
        # return link

    def delete_last_n_node(self, n):
        """删除链表中倒数第N个节点.
        主体思路：
            设置快、慢两个指针，快指针先行，慢指针不动；当快指针跨了N步以后，快、慢指针同时往链表尾部移动，
            当快指针到达链表尾部的时候，慢指针所指向的就是链表的倒数第N个节点
        参数:
            n:需要删除的倒数第N个序数
        """
        # n的校验 1<= n <=self.length
        if n < 1 or n > self.length:
            raise ValueError("n的值错误")
        if n == self.length:

            self.head = self.head.next
            return

        fast = self.head
        slow = self.head
        step = 0

        while step < n:
            fast = fast.next
            step += 1
            
        while fast.next is not None:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next


    def has_ring(self):
        """
            判断链表是否有环

            思路:  通过快慢指针, 快指针一步跨2节点, 慢指针一步跨1节点, 如果存在环 快慢指针所指向节点一定会相遇
        :return:
        """

        fast = self.head
        slow = self.head

        while fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True

        return False

    def create_ring(self, n):
        """
            给无环链表构造一个环, 尾节点指向第n个节点
        :param n: 无环链表的第n个节点
        :return:  有环链表
        """
        if n < 0 or n >= self.length:

            raise ValueError("n值错误")

        cur = self.head
        if n == 1:
            while cur.next is None:
                cur = cur.next
            cur.next = cur
            return
        
        node_n = None  # 记录加环的节点
        i = 0
        while cur.next is not None:
            cur = cur.next
            i += 1
            if i == n:
               node_n = cur

        cur.next = node_n



if __name__ == '__main__':

    sll = SingleLinkList()
    sll.append(1)
    sll.append(2)
    sll.append(3)
    sll.append(4)
    sll.append(5)
    print(sll, f"长度:{sll.length}")

    sll.delete_last_n_node(5)

    print(sll, f"长度:{sll.length}")


    sll.create_ring(1)
    print(sll.has_ring())





