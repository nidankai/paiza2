input_arg = input().split(' ')
fish_num = int(input_arg[0])
poi_num = int(input_arg[1])
poi_life = int(input_arg[2])

fish_list = list()
for i in range(fish_num):
    fish_list.append(int(input()))

scooped_count = 0
now_poi_life = poi_life
poi_count = poi_num
for fish in fish_list:
    if fish < now_poi_life:
        now_poi_life -= fish
        scooped_count += 1
    else:
        poi_count -= 1
        if poi_count == 0:
            break
        now_poi_life = poi_life
        if fish < now_poi_life:
            now_poi_life -= fish
            scooped_count += 1
        else:
            poi_count -= 1
            if poi_count == 0:
                break
            now_poi_life = poi_life

print(scooped_count)
