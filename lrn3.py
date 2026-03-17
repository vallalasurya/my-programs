# check if first and last element of a list are same
x=[5,12,15,7,5]
def first_last(x):
    first=x[0]
    last=x[-1]
    if first==last:
        return True
    else:
        return False
print(first_last(x))        
 