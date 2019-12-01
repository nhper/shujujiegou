def bubble_sort(blist):
    '''
    冒泡排序,参数为无序列表
    :param blist:
    :return: 排序好的列表
    '''
    length = len(blist)
    for i in range(length-1):
        for j in range(1,length-i):
            if blist[j-1]>blist[j]:
                blist[j-1],blist[j] = blist[j],blist[j-1]
    return blist
# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        '''
        python中可以直接用in来进行逐行判断
        :param target:
        :param array:
        :return: True or False
        '''
        for i in array:
            if target in i:
                return True
        return False


if __name__ == '__main__':
    l = [8, 4, 9, 2, 5, 1, 6, 3, 7]
    l = bubble_sort(l)
    print(l)

