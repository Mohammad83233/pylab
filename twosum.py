def twonumbers(numbers,target):
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if numbers[i]+numbers[j]==target:
                print(i,j)
numbers=list(map(int,input("enter the numbers  \n").split()))
target=int(input("enter the target please .. \n"))
twonumbers(numbers,target)
