#2
#由两个堆栈组成的队列，add,poll,peek, 
#问题：__repr__函数无反应
class de_list():
    '''
    dfsdf
    '''
    def __init__(self,nums):
        self.stack1 = list(nums)
        self.stack2 = list([])
        for i in range(len(nums)-1,0-1,-1):
            self.stack2.append(self.stack1[i])
        
    def push(self,num):
        self.stack1.append(num)
        self.stack2 = list([])
        for i in range(len(self.stack1)-1,0-1,-1):
            self.stack2.append(self.stack1[i])
    
    def poll(self):
        self.stack2.pop()
        self.stack1 = list([])
        for i in range(len(self.stack2)-1,0-1,-1):
            self.stack1.append(self.stack2[i])
            
    def peek(self):
        return self.stack2[-1]

    def __repr__(self):
        return self.stack2
        
    def __str__(self):
        return print(self.stack2)
