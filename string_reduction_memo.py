#string dictionary
str_memo ={}



#checks the two letter value of the string and reduces using to one letter
def str_reduce(st):
    if st=='ab'or st =='ba' :
        return 'c'
    if st =='ca' or st =='ac' :
        return 'b'
    if st =='cb' or st =='bc' :
        return 'a'
    return st


def strReduce(a):
    answer =0 
    strlength=len(a)
    #length is 1
    if strlength ==1 and (a[0] =='a' or a[0] =='b' or a[0] =='c'):
        answer =1
    #length is 2
    if strlength ==2:
        #if it can be reduced length is 1
        twolenstr = str_reduce(a)
        #set length to length of new string
        answer =len(twolenstr)
    #if length is larger than 2 then we parse the string and modify accordingly
    if strlength>2:
        answer = len(a)
        #for loop for all values in the string
        for i in range(len(a)-1):
            #loop into if the character is not same as the character after it
            if a[i] !=a[i+1]:
                #substring of the 2 letters that aren't same and reduce it
                substr = a[i:i+2]
                new_string_st1=''
                new_string_st2=''
                reduced_str = str_reduce(substr)
                
                #create prefix of the new string to be appended
                if i==1:
                    new_string_st1= a[0]
                elif i>1:
                    new_string_st1=a[0:i]
                #create suffix of the new string to be appended
                if (i+2)<(len(a)-1):
                    new_string_st2= a[i+2:]
                elif (i+2)==(len(a)-1):
                    new_string_st2=a[i+2]
                #new string stord
                new_string = new_string_st1+reduced_str+new_string_st2
                #calculate min of new string recursively
                
                new_min = stringReduction(new_string)
                # if min of new string is smaller, set the answer to new min value
                if new_min<answer:
                    answer=new_min
    #return value of length
    return answer

#memoized solution
def stringReduction(a):
    #checks if a isn't in the dictionary
    if a not in str_memo:
        #stores a and all the reduced versions 
        #(because of the recursive calls) in the dictionary
        str_memo[a] = strReduce(a)
        str_len = str_memo[a]
    #sets length if it is in dictionary
    else:
        str_len = str_memo[a]

    return str_len

if __name__ == '__main__':
    t = int(input())
    result=''
    for i in range(0,t):
        a=input()
        result +=str(stringReduction(a))+'\n'
    #used for loop to see all values in look-up table
    #for k,v in str_memo.items():
    #   print(k,v)
    print(result.rstrip('\n'))