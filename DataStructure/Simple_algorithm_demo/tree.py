"""
二叉树的实现 python

"""


class Node:
    """二叉树节点"""

    def __init__(self, val):
        self.name = val
        self.lchild = None
        self.rchild = None


class Tree:
    """二叉树"""

    def __init__(self):
        self.root = None  # 二叉树的根

    def add(self, val):
        node = Node(val)
        if self.root is None:  # 判断二叉树是否为空
            self.root = node
            return
        queue = [self.root]  # 队列容器，存放子节点不为None的节点，用于循环中的搜索空节点位置
        while queue:
            curr_node = queue.pop(0)
            if curr_node.lchild is not None:  # 说明该节点的左子节点，不为空
                queue.append(curr_node.lchild)  # 添加进队列，下一次判断
            else:
                curr_node.lchild = node  # 该子节点为空，我们就可以把需要添加的节点，放在该位置
                return
            if curr_node.rchild is not None:  # 说明该节点的右子节点，不为空
                queue.append(curr_node.rchild)  # 添加进队列，下一次判断
            else:
                curr_node.rchild = node  # 该子节点为空，我们就可以把需要添加的节点，放在该位置
                return

    def traversing(self):
        """二叉树广度优先遍历"""
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            curr_node = queue.pop(0)
            print(curr_node.name, end=" ")  # 打印当前节点的值
            # 判断子节点是否为None,不为None则把子节点放入队列queue中，下一步循环时在打印
            if curr_node.lchild is not None:
                queue.append(curr_node.lchild)
            if curr_node.rchild is not None:
                queue.append(curr_node.rchild)

    def prevorder_traversing(self, node):
        """先序遍历"""
        if node is None:
            return
        print(node.name, end=" ")
        self.prevorder_traversing(node.lchild)
        self.prevorder_traversing(node.rchild)

    def infixorder_traversing(self, node):
        """中序遍历"""
        if node is None:
            return
        self.infixorder_traversing(node.lchild)
        print(node.name, end=" ")
        self.infixorder_traversing(node.rchild)

    def postorder_traversing(self, node):
        """后续遍历"""
        if node is None:
            return
        self.postorder_traversing(node.lchild)
        self.postorder_traversing(node.rchild)
        print(node.name, end=" ")


if __name__ == '__main__':
    tree = Tree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.traversing()  # 广度优先遍历
    print("")
    tree.prevorder_traversing(tree.root)  # 先序
    print("")
    tree.infixorder_traversing(tree.root)  # 中序
    print("")
    tree.postorder_traversing(tree.root)  # 后序
