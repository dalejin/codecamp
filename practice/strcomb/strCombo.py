
def strCombo(s, n):
	l = list(s)
	ret = list()
	#len is 1
	if len(s) ==1: 
		ret=[s]
	#case for len is 2
	elif len(s)==2:
		#add the string 
		ret= [s]
		#add each letter in the string
		ret+=[s[-1]]
		ret+=[s[-2]]
		#sort for lexicographical order
		ret.sort()
	#case for len is greater than 3
	else:
		#for every i from 1 to 1 shifted by n bits since (2^n) combinations
		for i in range(1,(2**n)):
			st =""
			#for all letters in n
			for j in range(0,n):
				#if the combo number & letter number !=0 enter loop
				if i&(2**j):
					#add the jth char to the string combo
					st= st+s[j]
			#add the string combination to the return list of combinations
			ret+=[st]		
		#sort the list for lexicographical order
		ret.sort()
	return ret

# Tail starts here
if __name__ == '__main__':
    t = int(input())
    result=''
    printlist=[]
    for i in range(0,t):
    	n = int(input())
    	s=input()
    	#call the combo function and add list to the total list
    	printlist=printlist+(strCombo(s, n))
    #print lists of all strings
    print('\n'.join(printlist))