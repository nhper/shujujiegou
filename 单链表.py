class ListNode(object):
    def __init__(self,val):
        self.val = val
        self.next = None

class Slist(object):
    def __init__(self):
        self.root = None
    def add(self,val):
        node = ListNode(val)
        if not self.root:
            self.root = node
            return
        root = self.root
        while root:
            if not root.next:
                root.next=node
                return
            root = root.next
    def printf(self):
        root = self.root
        l = []
        while root:
            l.append(root.val)
            root = root.next
        print(l)

if __name__ == '__main__':
    slist = Slist()
    for i in range(10):
        slist.add(i)
    slist.printf()


