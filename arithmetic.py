x=input("enter first number")
x=int(x)
y=input("enter second number")
y=int(y)

operation=input("enter the operation")

if operation == "+":
	result= int(x)+int(y)
	print(result)
elif operation == "-":
	result=int(x)-int(y)
	print(result)
elif operation == "*":
	result=int(x)*int(y)
	print(result)
elif operation =="/":
	result=int(x)/int(y)
	print(result)

else:
	print("enter correct operation")
