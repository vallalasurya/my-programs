'''rows=5
for i in range( rows ,0,- 1):  #4
     spaces= rows-i      #5-5=0 spaces
     stars=2*i-1         #2*5=10-1=9  stars
     print(" " * spaces + "*" *  stars)
   '''
rows=5
for i in range(1, rows+1):
        g= rows-i  #5-1=4
        s=2*i-1  #2*1-1=1
        print(" " *g + "*" * s  )