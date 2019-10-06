flower_num = int(input())
flowering_days = list()
for i in range(flower_num):
    flower_list = input().split(' ')
    flowering_days.append(int(flower_list[0]) + int(flower_list[1]))
flowering_days.sort()

result_dict = dict()
for day in flowering_days:
    result_dict[str(day)] = 0

for day in flowering_days:
    result_dict[str(day)] += 1

for key, value in result_dict.items():
    if value == max(result_dict.values()):
        print(key)
        break
