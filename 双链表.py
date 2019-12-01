class ListNode(object):
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

class Dlist(object):
    def __init__(self):
        self.root = None  # 头结点
    def add(self,val):
        node = ListNode(val)
        if not self.root:
            self.root = node
            return
        root = self.root
        while root:
            if not root.next:
                root.next=node
                node.prev = root
                return
            root = root.next
    def printf(self):
        root = self.root
        l = []
        while root.next:
            l.append(root.val)
            root = root.next
        l.append(root.val)
        print(l)
        l = []
        while root.prev:
            l.append(root.val)
            root = root.prev
        l.append(root.val)
        print(l)


if __name__ == '__main__':
    dlist = Dlist()
    for i in range(10):
        dlist.add(i)
    dlist.printf()


