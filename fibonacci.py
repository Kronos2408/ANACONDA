#print fibonacci series of 10 elements
def Fibonacci(): 
    f1=0
    f2=1
    for i in range(0,10):
    	ne=f1+f2
    	f1=f2
    	f2=ne
    	print(ne)
Fibonacci()