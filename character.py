a=['ab','cd','ef']
b=['af','ee','ef']
for i in range(len(a)):
    found=False
    for char in a[i]:
        if char in b[i]:
            found=True
            break
    if found:
        print("YES")
    else:
        print("NO")
