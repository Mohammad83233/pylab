def k_missing(arr,k):
    arr=sorted(set(arr))
    missing_count=0
    current=1
    i=0
    
    
    while True:
        if i<len(arr) and arr[i]==current:
            i+=1
        else:
            missing_count+=1
        if missing_count==k:
            return current
        current+=1
arr=[2,5,6,18,11]
k=5
inpt=k_missing(arr,k)
print(inpt)
    
