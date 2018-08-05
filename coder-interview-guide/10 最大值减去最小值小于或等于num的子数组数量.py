#10 
#最大值减去最小值小于或者等于num的子数组的数量
#本题的重点在于根据题干得到一些基本的结论：如果arr[i,j]满足，则其子数组必然满足，如果arr不满足，则包含这个数组的数组必然不满足
def get_Num(arr,num):
    ''' arr is a list
        num is the number of the condition'''
    res = 0
    for i in range(len(arr)):
        qmax = i
        qmin = i
        for j in range(i,len(arr)):
            if arr[j] > arr[qmax]:
                qmax = j
            if arr[j] < arr[qmin]:
                qmin = j
            if arr[qmax]-arr[qmin] <= num:
                continue
            else:
                res += j-i
                break
            if j == len(arr):
                res += j-i
                break
    return res    