typhoon_pos_list = input().split(' ')
person_num = int(input())

center_x = int(typhoon_pos_list[0])
center_y = int(typhoon_pos_list[1])
center_radius = int(typhoon_pos_list[2])
wind_radius = int(typhoon_pos_list[3])

for i in range(person_num):
    person_pos_list = input().split(' ')
    tmp_param = (int(person_pos_list[0]) - center_x) ** 2 + (int(person_pos_list[1]) - center_y) ** 2
    if center_radius ** 2 <= tmp_param <= wind_radius ** 2:
        print('yes')
    else:
        print('no')
