# arr=[1,2,3,4]
# sum=0
# for i in arr:
#     sum=sum+i
# print(sum)
def sum(arr,l):
    
    if l==0:
        return 0
    return arr[l-1]+sum(arr,l-1)
    
arr=[10,20,30,40]
l=len(arr)
print(sum(arr,l))