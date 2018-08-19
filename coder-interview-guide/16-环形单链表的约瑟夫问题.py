#输入环形单向链表的头结点与报数的值，返回最后生存下来的节点
#进阶：如果链表的节点数为N,返回O(n)的算法
#普通：1星，进阶：3星

#进阶题没有理解清楚


class node():
    def __init__(self,data):
        self.data = data
        self.next = None

def joesphusKill(head,m):
    if head is None or head.next is None:
        return head
    cur = head
    cur_count = 1
    while cur is not cur.next:
        if cur_count+1 == m:  #这里的加一是考虑细节的重要之处
            cur.next = cur.next.next
            cur = cur.next
            cur_count = 1
        else:
            cur = cur.next 
            cur_count += 1
    return cur

#test_data
test_data = node(1)
cur = test_data
for i in range(2,20):
    cur.next = node(i)
    cur = cur.next



