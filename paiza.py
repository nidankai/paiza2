man_num = int(input())
man_names = input().split(' ')

book_num = int(input())
man_book_list = list()
for i in range(book_num):
    input_list = input().split(' ')
    dic = {"man_name": input_list[0], "book_price": int(input_list[1])}
    man_book_list.append(dic)

result_dic = dict()
for num, man_name in enumerate(man_names):
    result_dic[man_name] = 0

for man_book in man_book_list:
    result_dic[man_book["man_name"]] += man_book["book_price"]

score_sorted = sorted(result_dic.items(), key=lambda x:x[1], reverse=True)
for value in score_sorted:
    print(value[0])

