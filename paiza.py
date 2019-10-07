dislike_num = input()
room_total = int(input())
room_list = list()
for i in range(room_total):
    room_list.append(input())

flag = False
for num in room_list:
    if dislike_num in num:
        pass
    else:
        print(num)
        flag = True
if flag is False:
    print('none')