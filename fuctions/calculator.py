import sys

def add(num1, num2):
	x = num1 + num2
	return x

def sub(num1, num2):
	y = num1 - num2
	return y

def mul(num1, num2):
	z= num1 * num2
	return z

def div(num1, num2):
	a = num1 / num2
	return a

num1 = float(sys.argv[1])
operations = sys.argv[2]
num2 = float(sys.argv[3])

if operations == "add":
	output = add(num1,num2)
	print(output)

if operations == "mul":
	output = mul(num1,num2)
	print(output)

if operations == "sub":
	output = sub(num1,num2)
	print(output)

if operations == "div":
	output = div(num1,num2)
	print(output)


