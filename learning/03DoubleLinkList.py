# coding=utf8
class Node(object):
    def __init__(self, item):
        self.prev = None
        self.elem = item
        self.next = None


class DoubleLinkList(object):
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        return self.__head == None

    def length(self):
        cur = self.__head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """
        遍历链表
        """
        cur = self.__head
        while cur:
            print(cur.elem, end=" ")
            cur = cur.next
        print("")

    def add(self, item):
        """
        在链表头添加元素
        param item: 要添加的元素
        """
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            node.next = self.__head
            self.__head.prev = node
            self.__head = node

    def append(self, item):
        """
        在链表尾添加元素
        param elem: 要添加的元素
        """
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self, pos, item):
        """
        在指定位置添加元素
        param pos:
        param elem:
        """
        if pos <= 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            pre = self.__head
            count = 0
            while count < pos - 1:
                count += 1
                pre = pre.next
            node = Node(item)
            node.next = pre.next
            pre.next.prev = node
            pre.next = node
            node.prev = pre

    def remove(self, item):
        """
        删除制定元素
        param itme: 要删除的元素
        """
        cur = self.__head
        pre = None
        while cur:
            if cur.elem == item:
                if pre:
                    if cur.next:
                        pre.next = cur.next
                        cur.next.prev = pre
                    else:
                        pre.next = None
                else:
                    if cur.next:
                        cur.next.prev = None
                        self.__head = cur.next
                    else:
                        self.__head = None
                break
            pre = cur
            cur = cur.next

    def contain(self, item):
        cur = self.__head
        while cur:
            if cur.elem == item:
                return True
            cur = cur.next
        return False


def main():
    dll = DoubleLinkList()
    dll.add(1)
    dll.add(2)
    dll.append(3)
    dll.remove(2)
    dll.travel()
    print(dll.length())


if __name__ == '__main__':
    main()
