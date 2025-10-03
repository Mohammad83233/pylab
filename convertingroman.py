def intoRoman(num):
    values=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
    Symbols=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    result=""
    
    for i in range(len(values)):
        count=num//values[i]
        
        if count>0:
            result+=Symbols[i]*count
            num-=values[i]*count
    return result
    
input=int(input("enter a number : "))
roman=intoRoman(input)
print(roman)
