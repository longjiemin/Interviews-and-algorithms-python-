#分别实现翻转单项链表与双向链表
#难度：1星
#思路：注意1,2,3,4中1,4，的循环与2，3的循环

class Node():
    def __init__(self,data):
        self.data = data
        self.next = next
    
def reverseList(head):
    pre = None
    next = None
    while head is not None:
        next = head.next #1
        head.next = pre  #2
        pre = head  #3
        head = next  #4
        #1,4互相循环，head = head.next,不断迭代
        #2,3互相循环，new pre = old pre
    return pre

class DoubleNode():
    def __init__(self,data):
        self.data = data
        self.pre = None
        self.next = None

def reverseDoubleList(head):
    pre = None
    next = None
    while head is not None:
        next = head.next
        head.next = pre
        head.last = next #相对于单链表的变化点，保证下一级到上一级的链接不发生错误
        pre = head 
        head = next
    return pre 

    