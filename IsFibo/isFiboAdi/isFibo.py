import sys



#func def for checking if number is a fibonacci number
def isFibo(n):
	i = 2
	fib = []
	fib.append(0)
	fib.append(1)
	#while loop for fib list
	while fib[i-1]<n:
		fib.append(fib[i-1] + fib[i-2])
		i+=1
	#check if number is in fibonacci sequence
	if(fib[i-1] == n):
		return True
	else:
		return False


#takes input of T
input_list = []
print ("Please enter input size on the first line \nand the values on the following lines.\nFirst number should be between 1 and 105. \nThe following values between 1 and 1010. \nEmpty line will crash the program.")

while True:
	
	input_size = input("")
	while input_size == "" or input_size.isdigit()==False:
		input_size= input("Please enter a number for input size (range 1-105).\n")

	input_size = int(input_size)


	#checks for size of T
	if 1<=input_size<=105:
		for x in range(0, input_size):
			#asks values for T numbers
			input_str = input("")
			while input_str==""or input_str.isdigit()==False:
				input_str = input("Please enter a number for the fibonacci test (range 1-1010.\n")
			input_num = int(input_str)
			if 1<=input_num<=1010:
				#appends to list if value is correct
				input_list.append(input_num)
			else:
				while (1>int(input_str) or int(input_str)>1010):
					input_str = input("Value not in range. Please enter a value between 1 and 1010. \n")
				input_list.append(int(input_str))
	else:
		print ( "Input size not in range. Please run again with a value between 1 and 105 for input size.")
	break

# calls function that checks which numbers in the input are fibonacci numbers.
#printing is done here
for index in range(len(input_list)):

	if (isFibo(input_list[index]))==True:
		print ("IsFibo");
	else:
		print ("IsNotFibo");




