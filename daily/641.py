class ListNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class MyCircularDeque:

    def __init__(self, k: int):
        node = ListNode('#')
        self.head = None
        self.tail = None
        self.count = 0
        self.k = k

    def insertFront(self, value: int) -> bool:
        if self.count >= self.k: return False
        elif self.count == 0:
            node = ListNode(value)
            self.head = node
            self.tail = node
            self.count += 1
            return True
        else:
            node = ListNode(value)
            node.right = self.head
            self.head.left = node
            self.head = node
            self.count += 1
            return True

    def insertLast(self, value: int) -> bool:
        if self.count >= self.k: return False
        elif self.count == 0:
            node = ListNode(value)
            self.head = node
            self.tail = node
            self.count += 1
            return True
        else:
            node = ListNode(value)
            self.tail.right = node
            node.left = self.tail
            self.tail = node
            self.count += 1
            return True
        

    def deleteFront(self) -> bool:
        if self.count == 0: return False
        else:
            self.head = self.head.right
            self.count -= 1
            return True
        

    def deleteLast(self) -> bool:
        if self.count == 0: return False
        else:
            self.tail = self.tail.left
            self.count -= 1
            return True
        

    def getFront(self) -> int:
        if self.count > 0:
            return self.head.val
        else:
            return -1
        

    def getRear(self) -> int:
        if self.count > 0:
            return self.tail.val
        return -1

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
