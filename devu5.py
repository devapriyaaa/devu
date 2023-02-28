mark=input("enter your mark")
mark=int(mark)
if mark>24:
	print("you are passed")
	if mark>90:
		print("you have an A+") 
	else:
		print("You don't have an A+")
else:
	print("you have failed")
