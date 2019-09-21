arg_list = input().split(' ')
amount = int(arg_list[0])
fresh_sold_per = int(arg_list[1])
processed_sold_per = int(arg_list[2])

remain_amount = amount - amount * (fresh_sold_per * 0.01)
remain_amount = remain_amount - remain_amount * (processed_sold_per * 0.01)

print(remain_amount)
