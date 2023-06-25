arr=[10,20,30,40,50,60,70,80,90]
for i in range(len(arr)//2):
    arr[i],arr[len(arr)-i-1]=arr[len(arr)-1-i],arr[i]
print(arr)
# rev=arr[::-1]
# print(rev)