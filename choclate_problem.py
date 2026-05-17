def choclate(arr,n):
    result=[]
    count=0
    for i in range(n):
        if arr[i]!=0:
            result.append(arr[i])
        else:
            count+=1
    for i in range(count):
        result.append(0)
        
    return result
    
n=int(input())
arr=list(map(int,input().split()))
print(choclate(arr,n))
