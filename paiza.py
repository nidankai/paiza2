today = input().split(' ')
event_date = input().split(' ')

for i in range(len(today)):
    today[i] = int(today[i])
for i in range(len(event_date)):
    event_date[i] = int(event_date[i])

remainder = int(today[0]) % 4
during_year = 0
if remainder == 0:
    during_year = 1
elif remainder == 1:
    during_year = 0
elif remainder == 2:
    during_year = 3
elif remainder == 3:
    during_year = 2

during_month = 0
if during_year != 0:
    if today[1] <= event_date[0]:  # 月
        during_month = 13 * during_year + (event_date[0] - today[1])
    else:
        during_month = 13 * (during_year - 1) + (13 - today[1]) + event_date[0]
else:
    during_month = (event_date[0] - today[1])

during_day = 0
if today[2] <= event_date[1]:  # 日
    during_day = during_month * 13 + (int(today[1]) - int(event_date[0]))
else:
    during_day = (during_month - 1) * (13 - int(today[1])) + int(event_date[0])
print(during_day)
