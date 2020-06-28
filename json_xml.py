import json

def print_sorted_data(data, count):
    data_list = list(data.items())
    data_list.sort(key=lambda i: i[1], reverse=True)
    for i in range(count):
        print(f'{i+1} место. Слово: "{data_list[i][0]}". Количество повторений: {data_list[i][1]} раз')

with open('newsafr.json', encoding = 'utf-8') as f:
    data = json.load(f)
    word_dict = {}
    for news in data["rss"]["channel"]["items"]:
        for word in news["description"].split():
            if len(word) > 6:
                if word in word_dict:
                    word_dict[word] += 1
                else:
                    word_dict.setdefault(word, 1)

print_sorted_data(word_dict, 10)