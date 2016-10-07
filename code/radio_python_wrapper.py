import subprocess
import crcmod

rtl = subprocess.Popen(['rtl_fm', '-M', 'usb', '-f', '434.100M', '-s', '48k'],stdout=subprocess.PIPE)
sox = subprocess.Popen(['sox', '-t', 'raw', '-r', '48k', '-e', 's', '-b', '16', '-c', '1', '-V1', '-', '-t', 'wav', '-'],stdin=rtl.stdout, stdout=subprocess.PIPE)
minimodem = subprocess.Popen(['minimodem', '--rx', '-a', '300', '--stopbits', '2', '-8', '--quiet', '-f' '-'], stdin=sox.stdout,stdout=subprocess.PIPE)

success = 0
fail = 0

def crc16_ccitt(data):
    crc16 = crcmod.predefined.mkCrcFun('crc-ccitt-false')
    return hex(crc16(data))[2:].upper().zfill(4)

for line in iter(minimodem.stdout.readline, ''):
    fail += 1
    print('Fail:Success ratio = {0}:{1}'.format(fail,success))
    try:
        parity = line.decode('utf-8').split(',')[-1].split('*')[1].rstrip()
        data = line.decode('utf-8').replace("$","")[0:-6]
        if crc16_ccitt(str.encode(data)) == parity:
            print('YEAH GOT IT:',data)
            success += 1
            fail -= 1
    except:
         pass
