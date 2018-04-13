class Tree(object):
    def __init__(self, element=None):
        self.element = element
        self.left = None
        self.right = None

    def traversal(self):
        """
        树的遍历
        """
        print(self.element)
        if self.left is not None:
            self.left.traversal()
        if self.right is not None:
            self.right.traversal()

    def reverse(self):
        """
        树的翻转
        """
        self.left, self.right = self.right, self.left
        if self.left is not None:
            self.left.reverse()
        if self.right is not None:
            self.right.reverse()


def test():
    # 手动构建二叉树
    t0 = Tree(0)
    t1 = Tree(1)
    t2 = Tree(2)
    t0.left = t1
    t0.right = t2
    # 遍历
    t0.traversal()
    # 翻转
    t0.reverse()
    t0.traversal()


if __name__ == '__main__':
    test()