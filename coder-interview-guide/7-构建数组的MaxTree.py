#7
#生成窗口最大值数组，输入参数数组arr,窗口大小W, 输出一个长度为n-w+1的数组res
#使用O(N)的算法实现
#功能算法基本实现，并满足复杂度要求
def getmax_window(nums,w):
    res = []
    qmax = []
    for i in range(len(nums)):
        while len(qmax) !=0 and nums[i]>nums[qmax[-1]]:
            qmax.pop()
        qmax.append(i)
        if i-qmax[0] == w:
            qmax=qmax[1:]
        if i >= w-1:
            res.append(nums[qmax[0]])
    return res
        

  