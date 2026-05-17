def seeBoard(height):
    count=0
    Max_height=0
    
    for i in range(len(height)):
        if height[i] > Max_height:
            count+=1
            Max_height=height[i]
    return count
num=int(input("enter the no"))
height=list(map(int,input().split()))
print(seeBoard(height))
