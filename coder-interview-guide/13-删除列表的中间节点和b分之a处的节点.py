#给定链表的头结点，删除中间节点的函数；删除b/a处的节点
#难度：1星
#思路：去索引a,b其中a,步长为1，b步长为2,

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

def removeMidNode(head):
    if head.next is None:
        return head
    if head.next.next is None:
        return head.next
    a_cur = head
    b_cur = head.next.next  #这里的值的初始化是关键
    while b_cur.next is not None and b_cur.next.next is not None:  #这里隐含了与规则的知识
        a_cur = a_cur.next
        b_cur = b_cur.next.next
    a_cur.next = a_cur.next.next
    return head

def removeA_BNode(head,a,b):
    length = 0
    cur = head
    while cur.next is not None:
        length += 1
        cur = cur.next
    cur_index = int(a/b) + 1
    cur = head
    if length  == 1:
        head = head.next
        return head
    elif length ==3:
        head.next =None
        return head
    while cur_index-2 > 0:
        cur = cur.next
        cur_index -= 1
    cur.next = cur.next.next
    return head
         
        

    
