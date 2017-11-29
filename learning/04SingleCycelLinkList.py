# coding:utf8
class Node(object):
    """"
        this single link list node
    """

    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleLinkList(object):
    def __init__(self, node=None):
        self.__head = node
        if node:
            node.next = node

    def is_empty(self):
        """
        判断链表是否为空
        return: 链表是否为空
        """
        return self.__head is None

    def length(self):
        """
        返回链表长度
        return: 返回链表长度
        """
        cur = self.__head
        count = 0
        while cur:
            count += 1
            if cur.next is self.__head:
                break
            cur = cur.next
        return count

    def travel(self):
        """
        遍历链表
        """
        cur = self.__head
        while cur:
            print(cur.elem, end=" ")
            if cur.next is self.__head:
                break
            cur = cur.next

    def add(self, item):
        """
        在链表头添加元素
        param item: 要添加的元素
        """
        node = Node(item)
        cur = self.__head
        if cur is None:
            node.next = node
        else:
            node.next = cur
            # 找到最后一个节点
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
        self.__head = node

    def append(self, item):
        """
        在链表尾添加元素
        param elem: 要添加的元素
        """
        node = Node(item)
        cur = self.__head
        if cur is None:
            self.add(item)
        else:
            node.next = self.__head
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node

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
            while count < (pos - 1):
                count += 1
                pre = pre.next
            # 循环推出后 pre指向 pos前一个节点
            node = Node(item)
            node.next = pre.next
            pre.next = node

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
                    pre.next = cur.next
                    while cur.next != self.__head:
                        cur = cur.next
                    cur.next = self.__head
                else:
                    # 找到最后一个节点
                    last = self.__head
                    while last.next != self.__head:
                        last = last.next
                    last.next = cur.next
                    self.__head = cur.next
                break
            if cur.next is self.__head:
                break
            pre = cur
            cur = cur.next

    def search(self, item):
        cur = self.__head
        while cur:
            if cur.elem == item:
                return True
            if cur.next is self.__head:
                break
            cur = cur.next
        return False


def main():
    list = SingleLinkList()
    list.add(100)
    list.add(2100)
    list.append(134)
    list.insert(1, 10000)
    list.insert(1, 1000)
    list.insert(1, 12130)
    list.insert(2, 123)
    list.insert(0, 123)
    list.remove(134)
    # print(list.length())
    print(list.search(100))
    list.travel()


if __name__ == '__main__':
    main()
