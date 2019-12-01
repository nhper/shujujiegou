def hebing(l1,l2):
    result = []
    while l1 and l2:
    # 1. 取出l1 l2的元素
        key1 = l1[0]
        key2 = l2[0]
    # 2. 比较两个元素的大小  将小的元素放入结果列表
    # 3. 从刚才放入小的列表中再取出一个元素进行比较
        if key1<key2:
            result.append(l1.pop(0))
        else:
            result.append(l2.pop(0))
    # 4. 重复2-3
    # 5. 当l1或l2有一个为空的时候，结束比较 将l1或l2的剩余元素直接放到结果列表
    return result+l1+l2


def guibing(l):
    if len(l)<2:
        return l
    # 1.将列表拆分，一分为二
    mid = len(l)//2
    # 2.将左右的小列表进行归并排序
    left = guibing(l[:mid])
    right = guibing(l[mid:])
    # 3.返回合并的之后的列表
    return hebing(left, right)
    # 4.当列表长度小于2的时候 递归收敛


if __name__ == '__main__':
    # l1 = [1, 3, 5, 7, 9]
    # l2 = [2, 4, 6, 8, 10]
    # l = hebing(l1, l2)
    # print(l)
    import random
    l = list(range(10))
    random.shuffle(l)
    print(l)
    # l = [223,332,332,134,456]
    l = guibing(l)
    print(l)