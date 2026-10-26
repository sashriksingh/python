def common(list1,list2):
    common=[]
    for i in list1:
        if i in list1:
            if(i in list2):
                common.append(i)
    print(common)
common([2,4,6,8,10], [1,2,3,4,5,6,7,8,9,10])

