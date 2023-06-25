arr=[1,12,131,141,11111]
maxi=0

for i in arr:
    rev=0
    temp=i
    while i>0:
        sum=i%10
        rev=rev*10+sum
        i=i//10
    
    if rev==temp:
        if temp>maxi:
            maxi=temp
print(maxi)
