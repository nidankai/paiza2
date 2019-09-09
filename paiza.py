arg_list = input().split(' ')
menu = int(arg_list[0])
member = int(arg_list[1])

calorie_list = list()
for i in range(menu):
    calorie_list.append(int(input()))

for i in range(member):
    order_list = list()
    input_order_list = input().split(' ')
    for j in range(len(input_order_list)):
        order_list.append(int(int(input_order_list[j]) * calorie_list[j] / 100))
    sum_str = str(sum(order_list))
    print(sum_str)
