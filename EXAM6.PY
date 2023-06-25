def distribute_bills(N, amount_array):
    
    # amount_array.sort(reverse=True)
    
    for j in range(len(amount_array)-1):
        for i in range(len(amount_array)-1-j):
            if amount_array[i]<amount_array[i+1]:
                amount_array[i],amount_array[i+1]=amount_array[i+1],amount_array[i]
            else:
                pass 
   
  
    sums = [0] * N
    
   
    for i in range(len(amount_array)):
        
        min_sum_index = sums.index(min(sums))
        
        
        sums[min_sum_index] += amount_array[i]
        
        
    return sums


N = int(input())
amount_array=[]
amount=int(input())
for i in range(amount):
    amount_array.append(int(input()))

sums = distribute_bills(N, amount_array)
print(sums)

# Compute the maximum difference between the sums
max_diff = max(sums) - min(sums)
print(max_diff)