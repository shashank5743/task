def common(l1, l2): 
    l1_set = set(l1) 
    l2_set = set(l2) 
    if (l1_set & l2_set): 
        print(l1_set & l2_set)
    else: 
        print("No common elements")
    print((l1_set).difference(l2_set))# L1 not in L2.

l1 = ['a','b','c'] 
l2 = ['b','d'] 
common(l1, l2)
