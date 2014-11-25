import math

#Profit of selling pumpj at city and coming back
def calcProfit( x, y, price, d, c):
    dist = calcDistbwCities(x,y,0,0)
    return (((price*d) - ((1+c)*dist)), x, y, price)

#distance between 2 cities
def calcDistbwCities(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2 )

#find the best path        
def calcOptimalPath(profit):
    retstring = ''
    for p, x, y, price in profit:
        retstring += str(x)+ ' '+str(y) + ' 1'+ '\n' + '0 0' +'\n'
    return retstring

#calculates path to take
def calcPath(n, c, d, x, y, pumpjPrice):
    #stores x, y, and price in a tuple list
    listofAll = []
    for _ in range(n):
        listofAll.append((x[_], y[_], pumpjPrice[_]))
    #calculates the profit for all cities  
    profit =[]
    profit = [calcProfit( x[_],y[_],pumpjPrice[_], 1,c) for x[_],y[_],pumpjPrice[_] in listofAll]
    #arranges list by maximum profit 
    profit.sort()
    profit.reverse()

    #removes cities with negative profit for traveling
    profit=[(prof, x, y, price) 
            for (prof, x, y , price) in profit
                 if prof>10 ]
    #print (profit)
    retstring=''
    #used to find the order of the path to take        
    retstring = calcOptimalPath(profit)

    return retstring

if __name__ == '__main__':
    a=[]
    x=[]
    y=[]
    pumpjPrice=[]
    #stores n, c, d variables. need to use float for d input
    n, c, d = [float(i) for i in input().split()]
    #convert n and c to integer values
    n= int(n)
    #store x, y, pumpjack price
    for j in range(0,n):
        a +=input().split(" ")
        x+=[a[j*3]]
        y+=[a[j*3+1]]
        pumpjPrice+=[a[j*3+2]]
    #convert from list of string to ints
    x=list(map(int, x))
    y=list(map(int, y))
    pumpjPrice=list(map(int, pumpjPrice))
    #call calcPath to figure out the path to take
    result = calcPath(n, c, d, x, y, pumpjPrice)
    print (result.rstrip('\n'))
