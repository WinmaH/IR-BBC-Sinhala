import json

with open('/home/winma/Documents/Information-Retrieval/testInfo/news.json') as ob:
    data = json.load(ob)

with open('/home/winma/Documents/Information-Retrieval/unicode-converter/bbc_news.json', 'w') as ob1:
    json.dump(data, ob1, ensure_ascii=False)
