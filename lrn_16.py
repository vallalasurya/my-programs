n = [0, -1, 2, -3, 4, 0, 5]


pos_count=0
neg_count=0
zero_count=0
even_count=0
odd_count=0
for num in n:
    if num>0:
        pos_count+=1
    elif num<0:
        neg_count+=1
    else:
        zero_count+=1
    if num%2==0:
        even_count+=1
    else: 
        odd_count+=1    
print("positive:",pos_count)
print("negative:",neg_count)
print("zeroes:",zero_count)
print("even:",even_count)
print("odd:",odd_count)