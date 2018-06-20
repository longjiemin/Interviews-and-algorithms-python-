# -*- coding: utf-8 -*-
"""
Created on Fri May 11 19:41:34 2018

@author: longjiemin
"""

def solution():
    node_num = raw_input()
    node_num = int(node_num) #输入node数，转为整形
    edge = raw_input()
    edge = edge.split('\n')
    edge_list = []
    for k in edge:
        for i,j in k.split():
            edge_list.append([i,j])#将输入的edge保存到list中
    edge_dict = {}


    for i,j in edge_list:  #将所有的node的路径保存进一个字典中，key是出发点，node是所有可能到达的结束点
        if i in edge_dict.keys():
            edge_dict[i] = edge_dict[i].append(j)
        else:
            edge_dict[i] = [j]

    def get_num_sum(key,depth):
        if key not in edge_dict.keys():
            return 0
        else:
            return len(edge_dict[key])*depth+sum([get_num_sum(i,depth+1) for i in edge_dict[key]])
            
            
        
    for i in range(node_num): #对每一节点做一次遍历，寻找以该节点开始的路径数目
        sum_list = []          #将每一个节点的路径总数保存进list中
        sum_list.append(get_num_sum(i,1))
    
    return max(sum_list)
            
