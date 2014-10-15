#!/usr/bin/py
# Head ends here
string_memo = {}
def stringMemo(a):
    if not a in string_memo:
        string_memo[a]= stringReduction(a)
    
    for k, v in string_memo.items():
        print ("sup \n" )
        print (k, v)
    return string_memo[a]



#uses memoization to keep a list of reduced strings.
def stringReduction(a):
    answer =len(a)
    #put the string in a list
    strlist = [a]
    #while theres a string in the list go into loop
    while strlist: 
        #pop the string at the end of the list
        strval = strlist.pop()
        #check if strval is smaller than stored length before trying to further reduce it 
        if answer>len(strval):
            answer=len(strval)
        for i in range(len(strval)-1):
            #loop into if the character is not same as the character after it
            if strval[i] !=strval[i+1]:
                #take the substring of the values that are not equal 
                #from the shortened string popped off the end of list
                substr = strval[i:i+2]
                #check the values of the substring and edit them accordingly
                if substr=='ab'or substr =='ba' :
                    substr = 'c'
                if substr =='ca' or substr =='ac' :
                    substr = 'b'
                if substr =='cb' or substr =='bc' :
                    substr = 'a'
                #add the new shortened string back into the front of the 
                #list to see if it can be shortened further
                strlist.insert(0,strval[:i]+substr+strval[(i+2):])
    #return value of length
    return answer

# Tail starts here
if __name__ == '__main__':
    t = int(input())
    result=''
    for i in range(0,t):
        a=input()
        result +=str(stringMemo(a))+'\n'
    
    
    print(result.rstrip('\n'))