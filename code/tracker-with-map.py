## pip3 install crcmod
## sudo apt-get install python3-matplotlib
## sudo apt-get install python3-mpl_toolkits.basemap

import subprocess
import crcmod
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

rtl = subprocess.Popen(['rtl_fm', '-M', 'usb', '-f', '434.100M', '-s', '48k'],stdout=subprocess.PIPE)
sox = subprocess.Popen(['sox', '-t', 'raw', '-r', '48k', '-e', 's', '-b', '16', '-c', '1', '-V1', '-', '-t', 'wav', '-'],stdin=rtl.stdout, stdout=subprocess.PIPE)
minimodem = subprocess.Popen(['minimodem', '--rx', '-a', '300', '--stopbits', '2', '-8', '--quiet', '-f' '-'], stdin=sox.stdout,stdout=subprocess.PIPE)

success = 0
fail = 0

def crc16_ccitt(data):
    crc16 = crcmod.predefined.mkCrcFun('crc-ccitt-false')
    return hex(crc16(data))[2:].upper().zfill(4)

plt.ion()

for line in iter(minimodem.stdout.readline, ''):
    fail += 1
    print('Fail:Success ratio = {0}:{1}'.format(fail,success))
    try:
        parity = line.decode('utf-8').split(',')[-1].split('*')[1].rstrip()
        data = line.decode('utf-8').replace("$","")[0:-6]
        if crc16_ccitt(str.encode(data)) == parity:
            success += 1
            fail -= 1
            long, lat = data.split(',')[3], data.split(',')[4]
            my_map = Basemap(projection='robin', lat_0 = lat, lon_0 = long, resolution = 'l' , area_thresh = 1000.0, llcrnrlon=long-20, llcrnlat=lat-20, urcrnrlon=long+20, urcrnrlat=lat+20)
            my_map.drawcoastlines()
            my_map.drawcountries()
            my_map.fillcontinents(color='coral')
            plt.draw()
    except:
         pass
