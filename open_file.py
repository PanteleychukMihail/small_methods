import os


list_path = []

for adress, dirs, files in os.walk('g:\\'):
    for file in files:
        fullpath = os.path.join(adress, file)
        list_path.append(fullpath)

r = open('text.txt', 'w', encoding="utf-8")
for i in list_path:
    r.write(i + "\n")
r = open('text.txt',encoding="utf-8")

for i in r:
    if 'off23' in i:
        print (i)

r.close()