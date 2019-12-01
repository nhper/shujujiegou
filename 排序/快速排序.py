def quick_sort(qlist):
    if len(qlist)<2:
        return qlist
    s = qlist[-1]
    left = []
    right = []
    mid = []
    for i in qlist:
        if i<s:
            left.append(i)
        elif i>s:
            right.append(i)
        else:
            mid.append(i)
    left = quick_sort(left)
    right = quick_sort(right)
    return left+mid+right

if __name__ == '__main__':
    l = [8, 4, 9, 2, 5, 1, 6, 3, 7]
    l = quick_sort(l)
    print(l)
