def select_sort(slist):
    for i in range(len(slist)):
        for j in range(i+1,len(slist)):
            if slist[i]>slist[j]:
                slist[i],slist[j] = slist[j],slist[i]

    return slist


if __name__ == '__main__':
    l = [8, 4, 9, 2, 5, 1, 6, 3, 7]
    l = select_sort(l)
    print(l)