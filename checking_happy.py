def check_is_happy(number):
    sq=0
    n=number
    while n>0:
        sq+=(n%10)**2
        n=n//10
    if sq==1:
        print(f"the {number} is  a happy number")
    else:
        print(f"the {number} is not a happy number")
        
check_is_happy(100)
