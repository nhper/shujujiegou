class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


class Tree(object):
    def __init__(self):
        self.root = None

    def add(self,val):
        node = TreeNode(val)
        if not self.root:
            self.root = node
            return
        s = [self.root]
        while True:
            root = s.pop(0)
            if not root.left:
                root.left = node
                return
            s.append(root.left)
            if not root.right:
                root.right = node
                return
            s.append(root.right)
    def nlr(self,root):
        '''
        二叉树的前序遍历  根 左 右
        :param root:
        :return: 根+左+右
        '''
        if not root:
            return []
        n = [root.val]
        l = self.nlr(root.left)
        r = self.nlr(root.right)
        return n+l+r


    def lnr(self,root):
        '''
        二叉树的中序遍历  左根右
        :param root:
        :return: 左+根+右
        '''
        if not root:
            return []
        n = [root.val]
        l = self.lnr(root.left)
        r = self.lnr(root.right)
        return l+n+r

    def lrn(self,root):
        '''
        二叉树的后序遍历  左右根
        :param root:
        :return: 左+右+根
        '''
        if not root:
            return []
        n = [root.val]
        l = self.lrn(root.left)
        r = self.lrn(root.right)
        return l+r+n

    def cengci(self,root):
        '''
        二叉树的层序遍历 从上到下,从左到右
        :param root:
        :return:
        '''
        n = [root]
        s = []
        while n:
            root = n.pop(0)
            s.append(root.val)
            if root.left:
                n.append(root.left)
            if root.right:
                n.append(root.right)
        return s

    def jinxiang(self,root):
        '''
        二叉树镜像(左右翻转)
        :param root:
        :return:
        '''
        if not root:
            return
        root.left,root.right = root.right,root.left
        self.jinxiang(root.left)
        self.jinxiang(root.right)

    def treeDepth(self,root):
        '''
        求二叉树的最大深度
        :param root:
        :return:
        '''
        if not root:
            return 0
        left = self.treeDepth(root.left)
        right = self.treeDepth(root.right)
        return 1+max(left,right)


if __name__ == '__main__':
    tree = Tree()
    for i in range(1,10):
        tree.add(i)

    qianxu = tree.nlr(tree.root)
    zhongxu = tree.lnr(tree.root)
    houxu = tree.lrn(tree.root)
    cengxu = tree.cengci(tree.root)
    print(qianxu)
    print(zhongxu)
    print(houxu)
    print(cengxu)
    print('--------------------------镜像-----------------------------------------------')
    tree.jinxiang(tree.root)
    qianxu = tree.nlr(tree.root)
    zhongxu = tree.lnr(tree.root)
    houxu = tree.lrn(tree.root)
    cengxu = tree.cengci(tree.root)
    print(qianxu)
    print(zhongxu)
    print(houxu)
    print(cengxu)
    print(tree.treeDepth(tree.root))
