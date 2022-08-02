import os
import time

'''('d:\\torrent', ['Geroi.mecha.i.magii.3.klinok.armagedona.2000.PC', '[RePack by S.L.] Heroes of Might & Magic 3. HD Edition'], 
 ['Windows 10.iso', 'Windows.iso'])'''

spisok = []

for adress, dirs, files in os.walk(r'C:\Users\777\Desktop'):
    for file in files:
        full=os.path.join(adress, file)
        if time.time() - os.path.getctime(full ) < 1000000000:
            spisok.append(full)
print(spisok)