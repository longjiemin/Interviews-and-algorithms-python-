#给定链表的表头，判断是否为回文结构
#进阶：链表长度为n，时间复杂度为O（N),额外空间复杂度为O(1)
#难度:1星 进阶：2星
#思路：普通解法直接利用堆栈逆序链表即可，进阶解法一：

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

def isPalindromel(head):
    stack = []
    cur = head 
    while cur.next is not None:
        stack.append(cur)
        cur = cur.next
    cur = head
    while cur.next is not None:
        if cur != stack.pop():
            return False
    return True

#test_data
if __name__ == '__mian__':
    test_data1 = Node(1)
    test_data1.next=Node(2)
    test_data1.next = Node(1)
    test_data2 = Node(1)
    test_data2.next = Node(2)
    test_data2.next = Node(3)
    a=isPalindromel(test_data1)
    print(a)
    #print('tsst_data2:', isPalindromel(test_data2))