#amount of money that we have initially
money=100000
#reading data from file
data = open('sensex.csv','r')

#creating empty list to store the closing values
L=[]

for line in data:
    #appending the closing values into the list seprated by commas
    L.append(float(line.split(",")[-2]))

#initially giving values to both
max_value=0
min_value=0

for i in range(len(L)):
    if L[i]==min(L):
        min_value=i
    if L[i]==max(L):
        max_value=i

#defining a function to calculate profit
def profit(buy_price,sell_price):
    return money*(sell_price - buy_price)/buy_price

#applying the conditions of stock market
if (min_value < max_value):
    print("Buy at Rs.", L[min_value],"and sell at Rs.",L[max_value])
    print("profit is", profit(L[min_value],L[max_value]))

if (min_value > max_value):
    min_before_max = min(L[:max_value])

    max_after_min = max(L[min_value:])

#comparing the profits in two cases
if profit(min_before_max,L[max_value]) > profit(L[min_value],max_after_min):
    print("Buy at Rs.", min_before_max,"and sell at Rs.",L[max_value])
    print("profit is", profit(min_before_max,L[max_value]))

else:
    print("Buy at Rs.",min_before_max,"and sell at Rs.",max_after_min)
    print("profit is", profit(L[min_value], max_after_min)) 

    