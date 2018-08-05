#给定参数from,to，把链表中from到to的链表进行翻转
#难度：1星
#思路：先判断条件是否满足from,to的大小，找到翻转点的起点的前一个位置和终点的后一个位置，然后按照14的思路来写

class Node():
    def __inti__(self,data):
        self.data =data
        self.next = None
    
def reversePart(self,head,from_num,to_num):
    length = 0
    cur = head

    fPre =None
    tPos = None
    while cur is not None: #技巧
        length += 1 
        fPre = cur if length == from_num-1 else fPre
        tPos = cur if length == to_num -1 else tPos
        cur = cur.next

    if from_num >= 1 and to_num <= length and to_num > from_num:
        pass
    else:
        raise RuntimeError('error agr')

    node1 = fPre.next
    node2 = node1.next
    node1.next = tPos #先将原链表中的待翻转部分去掉
    next = None
    while node2 is not tPos:
        next = node2.next
        node2.next = node1  #类似于原先的全部翻转，但是起始点不是一个None了
        node1 = node2
        node2 = node2.next
    if fPre is not None:
        fPre.next = node1
        return head
    return node1



    

