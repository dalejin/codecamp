Problem Statement
-----------------
Quality Oil Well Pumpjack Inc. is looking to expand their sales to other cities (N), so they hired you as a salesman to fly to other cities to sell pumpjack. Pumpjacks can be expensive to travel with, so you will need to determine how many pumpjacks to take along with you on each trip and when to return to headquarters to get more. Quality Oil Well Pumpjack has an unlimited supply of pumpjack.

You will be able to sell only one pumpjack in each city you visit, but you do not need to visit every city, since some have expensive travel costs. Each city has an initial price that pumpjacks sell for, but this goes down by a certain percentage as more pumpjacks are sold (and the novelty wears off). Find a good route that will maximize profits.

Details
-------

Pumpjack Decline - The pumpjacks will decline (D) in price every time you visit 10% of the cities (the number of cities will always be a multiple of 10). For example, if D is .95 and there are 10 cities, then for every city you visit (except headquarters), the price of pumpjacks will be multiplied by .95. So after 5 visits, every city's pumpjack price will be about 77% of the initial value (.95^5).

Travel costs
------------
```
It costs the salesman $1/mile for his own travel.
Pumpjacks' travel costs are $C/Pumpjack/Mile. C is given as part of the input.
All distance costs are based on the real distance between two cities.
Quality Oil Well Pumpjack Headquarters is located at (0,0).
```
Input Format
------------
The first line of input for each test case will contain 3 parameters:
```
number of cities (N)
pumpjack cost per mile (C)
pumpjack factor of decline (D)
This will be followed by N lines, which will each contain 3 integers, for city location (x and y co-ordinates the grid, in miles) and the intial pumpjack sales price. 
- x y pumpjack_price
```
Constraints
-----------
```
(10≤ N ≤ 10^5)
(0.2 ≤ C ≤ 4) 
(0.5 ≤ D ≤ 0.99)
-1,000 < =x <= 1,000; -1,000 <= y <= 1,000
cost of a pumpjack < 10^5
```
Sample Input
------------
```
10 3 0.95
1 1 30
2 2 35
0 8 50
7 2 20
7 3 25
10 7 90
9 8 35
5 15 10
8 18 15
1 9 60
```
Output Format
-------------
On each line output the next city you are visiting (x,y). When leaving headquarters, also add the number of pumpjacks you are taking with you for that part of the trip. You do not need to return to headquarters when you finish your sales.

Sample Output
-------------
```
1 1 2
2 2
0 0
10 7 2
9 8
0 0
0 8 2
1 9
```
Explanation
-----------
The salesman first travels a distance of √2 dollars to (1,1) carrying 2 pumpjacks. This will cost him √2 dollars for his own travel and 6√2 dollars for the 2 pumpjacks. He will then earn 30 dollars selling 1 pumpjack. He then continues to (2,2) with only 1 pumpjack, which will cost him 1√2 dollars for his travel and 3√2 dollars for his pumpjack. He will then earn 33.25 dollars selling the pumpjack, since the prices have declined by 5%. After his return to HQ (a distance of 2√2) he will have earned an approximate profit of 44.87 dollars.

Scoring
-------
The goal of this challenge is to achieve the maximum profit on each test case. Your profits for each test case will be:
```
Total Pumpjack Sales - Total Travel Costs
```
You will receive a score for each test case based on the ratio of your profit to the estimated maximum profit. Your total score for this challenge will be a weighted sum of your scores for each test case. If your profit is negative, you'll receive zero score
