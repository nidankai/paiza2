budget, rides = input().split(' ')
budget = int(budget)
rides = int(rides)
price_list = list()
for i in range(rides):
    price = int(input())
    price_list.append(price)

point = 0
for price in price_list:
    if point >= price:
        point -= price
    else:
        budget -= price
        point += price * 0.1
    print(budget, int(point))

