receipt_num = int(input())
date_list = list()
fee_list = list()
for i in range(receipt_num):
    receipt_list = input().split(' ')
    date_list.append(receipt_list[0])
    fee_list.append(int(receipt_list[1]))

point = 0
for i in range(receipt_num):
    magnification = 0.01
    if '3' in date_list[i]:
        magnification = 0.03
    elif '5' in date_list[i]:
        magnification = 0.05
    point += int(fee_list[i] * magnification)

print(point)