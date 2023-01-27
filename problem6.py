squaredsum=0
sum=0
for i in range(101):
    sum = sum+i
    squaredsum=squaredsum+(i**2)
sum = sum**2
print(squaredsum-sum)