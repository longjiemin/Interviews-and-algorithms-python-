#8
#给定一个定义的二叉树节点类，对一个没有 重复元素的的list生成最大树
#要求时间复杂度为O(N)，空间复杂度为O(N)
#如下为给定二叉树定义：
#逻辑不难，代码实现有点复杂
class Node():
    def __init__(self,data=None,left=None,right=None):
        self.left = left
        self.right = right 
        self.data = data
        
        
