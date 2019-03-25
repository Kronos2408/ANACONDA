#calculate sum of three nos if the numbers are equal to each other then return o
x=int(input("enter value of a:"))
y=int(input("enter value of b:"))
z=int(input("enter value of c:"))
def sum(x,y,z):
	if x==y:
		return(0)
	elif y==z:
		return(0)
	elif z==x:
		return(0)
	elif x==y==z:
		return(0)
	else:
		return(x+y+z)

a=sum(x,y,z)
print(a)

