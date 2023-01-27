chainLen=[]
def recursive(num, counter, orig):
    counter+=1
    if num!=1:
        if num%2==0:
            num=num/2

        else:
            num = num*3 + 1
        recursive(num,counter,orig)
    else:
        chainLen.append([counter,orig])

for i in range(1,1000000):
    recursive(i,0,i)
print(max(chainLen))