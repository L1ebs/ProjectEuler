found=0
for a in range(1,1000):
    for b in range(1,1000):
        for c in range(1,1000):
            if(a+b+c==1000 and (a**2)+(b**2)==(c**2) and c>b and b>a):
                print(a)
                print(b)
                print(c)
                print(a*b*c)
                found=1
            if found==1:
                break
        if found==1:
                break
    if found==1:
                break