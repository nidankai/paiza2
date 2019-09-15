entry_list = input().split(' ')
entry_list.extend(input().split(' '))

time_list = input().split(' ')
final_list = list()
if time_list[int(entry_list[0]) - 1] < time_list[int(entry_list[1]) - 1]:
    final_list.append(int(entry_list[0]))
else:
    final_list.append(int(entry_list[1]))

if time_list[int(entry_list[2]) - 1] < time_list[int(entry_list[3]) - 1]:
    final_list.append(int(entry_list[2]))
else:
    final_list.append(int(entry_list[3]))
final_list.sort()

final_time_list = input().split(' ')
if final_time_list[0] < final_time_list[1]:
    print(final_list[0])
    print(final_list[1])
else:
    print(final_list[1])
    print(final_list[0])
