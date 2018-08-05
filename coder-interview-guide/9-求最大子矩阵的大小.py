#9
#求最大子矩阵的大小，给定矩阵map，其中的值只有0和1，求其中全是1的矩阵的1的数量
#测试数据如下
#hight_size暂时没有实现o(N）的算法
import numpy as np
map = np.array([[1,0,1,1],[1,1,1,1],[1,1,1,0]])

def maxsizefrommap(map):
    max_size = 0         #总的maxsize
    hight_size = [0]*map.shape[1]
    for i in range(map.shape[0]):
        this_row = list(map[i])
        max_size_row = 0    #每一行的maxsize
        for j in range(len(hight_size)):
            if this_row[j] == 0:
                hight_size[j] = 0
            else:
                hight_size[j] += 1
#O(N**2)实现hight_size的面积计算
        for j in range(len(hight_size)):
            width_right = 0
            for h in range(j,len(hight_size)):
                if hight_size[h] >= hight_size[j]:
                    width_right += 1
                else:
                    break
            width_left = 0
            for h in range(j,-1,-1):
                if hight_size[h] >= hight_size[j]:
                    width_left += 1
                else:
                    break
            width = width_left + width_right - 1
            
            max_size_row = max(max_size_row,width*hight_size[j])
        max_size = max(max_size,max_size_row)
    return max_size
