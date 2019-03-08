def funcl(a):
	print("hi")
	print("|Hello|","\n",a )
funcl("Prithvi reddy")


def func3(name,height,weight):
	BMI=(height+weight)/2
	print(name,"BMI is",BMI,"\n")
func3("Prithvi",185,69)

def func3(a,b,c):
	d=a+b+c
	print(a,b,c,d)
func3(2,5,6)


def func4(university="IITB"):
	print("i am in","\t",university)
func4("IITG")
func4("IITD")
func4()

def func5(a,b,c):
	d=a+b+c
	print(a,b,c,d)
func5(2,5,6)


def func6(a,b):
	print("hii other function")
	c=a+b
	return c
def func7():
	print("hello,i am going to call other function")
	s=func5(2,7)
	print("addition is",s)
	func7()

func3("namitha",160,49)