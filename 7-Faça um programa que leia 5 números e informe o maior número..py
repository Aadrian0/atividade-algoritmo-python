num1=float(input("digite o 1� numero--> "))
num2=float(input("digite o 2� numero--> "))
num3=float(input("digite o 3� numero--> "))
num4=float(input("digite o 4� numero--> "))
num5=float(input("digite o 5� numero--> "))
if (num1 >num2 and num1 > num3 and num1 > num4 and num1  >num5):
	print("o maior numero � o 1�-->", num1)
if (num2 >num1 and num2 > num3 and num2 > num4 and num2  >num5):
	print("o maior numero � o 2�-->", num2)
if (num3 >num2 and num3 > num1 and num3 > num4 and num3  >num5):
	print("o maior numero � o 3�-->", num3)	
elif (num4 >num2 and num4 > num3 and num4 > num1 and num4  >num5):
	print("o maior numero � o 4�-->", num4)	
else:
	print("o maior numero � o 5�-->", num5)