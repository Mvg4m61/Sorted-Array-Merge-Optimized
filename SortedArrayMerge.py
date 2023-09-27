import time
def merge():
    l1 = []
    l2 = []
    n = int(input("\nEnter number of elements in first array: "))
    for i in range(n):
        num = int(input("Enter element: "))
        l1.append(num)
    m = int(input("\nEnter number of elements in second array: "))
    for i in range(m):
        num = int(input("Enter element: "))
        l2.append(num)
    l1.sort()
    print(l1)
    l2.sort()
    print(l2)
    lm = []
    i=0
    j=0
    s = time.time()
    while((i<n) and (j<m)):
        if l1[i]<=l2[j]:
            lm.append(l1[i])
            i+=1
            
        else:
            lm.append(l2[j])
            j+=1        
    else:
        f = time.time()
        if i!=n:
            for k in range(i,n):
                lm.append(l1[k])
        else:
            for k in range(j,m):
                lm.append(l2[k])
    print("\nMerged and sorted list: ",lm)
    print("\nTime taken in seconds: ",f-s)
merge()