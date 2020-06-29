import json
import xml.etree.ElementTree as ET

def print_sorted_data(data_dict, count):
    data_list = list(data_dict.items())
    data_list.sort(key=lambda i: i[1], reverse=True)
    for i in range(count):
        print(f'{i+1} место. Слово: "{data_list[i][0]}". Количество повторений: {data_list[i][1]} раз')

# открытие json
with open('newsafr.json', encoding = 'utf-8') as f:
    data = json.load(f)
    word_dict_json= {}
    for news in data["rss"]["channel"]["items"]:
        for word in news["description"].split():
            if len(word) > 6:
                if word in word_dict_json:
                    word_dict_json[word] += 1
                else:
                    word_dict_json.setdefault(word, 1)

# открытие xml
parser = ET.XMLParser(encoding = 'utf-8')
tree = ET.parse('newsafr.xml', parser)
root = tree.getroot()
news_list = root.findall('channel/item/description')
word_dict_xml = {}
for news in news_list:
    for word in news.text.split():
        if len(word) > 6:
            if word in word_dict_xml:
                word_dict_xml[word] += 1
            else:
                word_dict_xml.setdefault(word, 1)

print_sorted_data(word_dict_json, 10)
print_sorted_data(word_dict_xml, 10)