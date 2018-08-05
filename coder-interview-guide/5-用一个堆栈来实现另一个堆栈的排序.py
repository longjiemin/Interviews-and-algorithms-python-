#5
#用一个堆栈实现另一个堆栈的排序，不允许额外变量
#功能实现，基本没有问题
def sort_another(nums):
    if len(nums)==0:
        return []
    stack2 = [nums.pop()]
    while len(nums)>0:
        cur = nums.pop()
        while len(stack2) != 0 and cur>stack2[-1] :
            nums.append(stack2.pop())
        stack2.append(cur)
    return stack2
