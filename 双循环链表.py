class ListNode(object):
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

class Dclist(object):
    def __init__(self):
        self.root = None  # 头结点
    def add(self,val):
        node = ListNode(val)
        if not self.root:
            self.root = node
            self.root.next = node
            self.root.prev = node
            return
        root = self.root
        while root:
            if root.next == self.root:
                root.next=node
                node.prev = root
                self.root.prev = node
                node.next = self.root
                return
            root = root.next
    def printf(self):
        root = self.root
        l = []
        k=20
        while k:
            l.append(root.val)
            root = root.next
            k-=1
        print(l)
        l = []
        k=20
        while k:
            l.append(root.val)
            root = root.prev
            k-=1
        print(l)


if __name__ == '__main__':
    dclist = Dclist()
    for i in range(10):
        dclist.add(i)
    dclist.printf()


