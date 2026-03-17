'''
i=1
while i<=10:
    print(i)
    i+=1
    '''
n=int(input("enter a number:"))
k=n
b=len(str(n))
sum1=0
while n!=0:
    r=n%10
    sum1=sum1+(r**b)
    n=n//10
if sum1==k:
    print("armstrong number")
else:
    print("not a armstrog number")        