
import sys

url_list = ['text.txt', 'text2.txt', 'text25.txt', 'text3.txt']
list_defect = []
list_info = []
try:
    for url in url_list:
        try:
            r = open(url, encoding="utf-8")
            list_info.append(r.read())
        except Exception:
            list_defect.append(url)
            sys.exit()
            continue
finally:
    r = open("save.txt", 'a', encoding="utf-8")
    for i in list_info:
        r.write(i)
    r.write(str(list_defect))
    r.close()
    print('я все записал')

print(list_defect)